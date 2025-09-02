from transformers import AutoProcessor, AutoModelForVision2Seq
from transformers import AutoTokenizer, AutoModelForCausalLM

_GRANITE_MODEL_ID = "ibm-granite/granite-vision-3.2-2b"

def get_granite_model():
    """Load and return the Granite vision processor and model."""
    processor = AutoProcessor.from_pretrained(_GRANITE_MODEL_ID)
    model = AutoModelForVision2Seq.from_pretrained(_GRANITE_MODEL_ID)
    return processor, model

# LLM for translation
_GRANITE_LLM_MODEL_ID = "ibm-granite/granite-3.3-2b-base"

def get_granite_llm_translation():
    """Load and return the Granite LLM tokenizer and model for translation or text generation."""
    tokenizer = AutoTokenizer.from_pretrained(_GRANITE_LLM_MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(_GRANITE_LLM_MODEL_ID)
    return tokenizer, model
