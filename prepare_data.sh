#!/bin/sh

set -x

export PYTHONPATH="${HOME}/work2/object_detection/tensorflow_models:$PYTHONPATH"
export PYTHONPATH="${HOME}/work2/object_detection/tensorflow_models/slim:$PYTHONPATH"

OUTPUT_DIR="output"
mkdir -p ${OUTPUT_DIR}

PYTHON="python"  # Path to the python installed.

###############################################################
# Prepare the symbol data, using the 53-symbols ontology.
###############################################################
$PYTHON "tools/prepare_symbol_data.py" \
  --symbol_raw_annot_path="data/train/Symbols_train.json" \
  --output_json_path="output/symbol_train.json" \
  || exit -1

$PYTHON "tools/prepare_symbol_data.py" \
  --symbol_raw_annot_path="data/test/Symbols_test.json" \
  --output_json_path="output/symbol_test.json" \
  || exit -1

###############################################################
# Prepare the vocabulary and initial embedding matrix for:
#   1) Ads action-reason annotations;
#   2) Densecap annotations;
#   3) Symbol annotations.
###############################################################

# 1) Ads action-reason annotations;
$PYTHON "tools/prepare_action_reason_vocab.py" \
  --min_count=1 || exit -1
$PYTHON "tools/prepare_word_embedding.py" \
  --vocab_path="output/action_reason_vocab.txt" \
  --output_emb_path="output/action_reason_vocab_200d.npy" \
  --output_vocab_path="output/action_reason_vocab_200d.txt" \
  || exit -1

# 2) Densecap annotations;
$PYTHON "tools/prepare_densecap_vocab.py" \
  --min_count=1 || exit -1
$PYTHON "tools/prepare_word_embedding.py" \
    --vocab_path="output/densecap_vocab.txt" \
    --output_emb_path="output/densecap_vocab_200d.npy" \
    --output_vocab_path="output/densecap_vocab_200d.txt" \
    || exit -1

# 3) Symbol annotations.
$PYTHON "tools/prepare_symbol_list.py" \
  --symbol_cluster_path="data/additional/clustered_symbol_list.json" \
  || exit -1
$PYTHON "tools/prepare_word_embedding.py" \
  --vocab_path="output/symbol_vocab.txt" \
  --output_emb_path="output/symbol_vocab_200d.npy" \
  --output_vocab_path="output/symbol_vocab_200d.txt" \
  || exit -1

###############################################################
# Extract Inception V4 features.
# Warning: this will cost a long time to run!!!
###############################################################
export CUDA_VISIBLE_DEVICES=1
$PYTHON "tools/prepare_img_features.py" \
  --action_reason_annot_path="data/train/QA_Combined_Action_Reason_train.json" \
  --image_dir="data/train_images/" \
  --output_feature_path="output/img_features_train.npy" \
  || exit -1

$PYTHON "tools/prepare_img_features.py" \
  --action_reason_annot_path="data/test/QA_Combined_Action_Reason_test.json" \
  --image_dir="data/test_images/" \
  --output_feature_path="output/img_features_test.npy" \
  || exit -1

$PYTHON "tools/prepare_roi_features.py" \
  --bounding_box_json="output/symbol_box_train.json" \
  --image_dir="data/train_images/" \
  --output_feature_path="output/roi_features_train.npy" \
  || exit -1

$PYTHON "tools/prepare_roi_features.py" \
  --bounding_box_json="output/symbol_box_test.json" \
  --image_dir="data/test_images/" \
  --output_feature_path="output/roi_features_test.npy" \
  || exit -1

$PYTHON "tools/prepare_roi_features.py" \
  --bounding_box_json="output/densecap_train.json" \
  --image_dir="data/train_images/" \
  --output_feature_path="output/densecap_roi_features_train.npy" \
  || exit -1

$PYTHON "tools/prepare_roi_features.py" \
  --bounding_box_json="output/densecap_test.json" \
  --image_dir="data/test_images/" \
  --output_feature_path="output/densecap_roi_features_test.npy" \
  || exit -1

exit 0