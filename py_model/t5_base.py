import torch
from transformers import T5TokenizerFast, T5ForConditionalGeneration

import time
from loguru import logger

model = T5ForConditionalGeneration.from_pretrained('models/t5_base_final/model/')
tokenizer = T5TokenizerFast.from_pretrained('models/t5_base_final/model/tokenizer')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

def gentext(input_text, max_new_tokens_=64):
    prompt = input_text
    # 입력 텍스트를 토큰화
    text_input = tokenizer(prompt, return_tensors='pt', padding=True).to(device)

    # 모델을 GPU로 이동
    with torch.no_grad():
        outputs = model.generate(
            text_input['input_ids'],
            attention_mask=text_input['attention_mask'],
            max_new_tokens=max_new_tokens_,
            num_beams=1,
            top_k=50,
            top_p=0.95,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            temperature=1.1,
        )
        
    # 예측 결과 디코딩
    predicted_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
    logger.info(f'입력 : {input_text} \n출력: {predicted_text}')
    
    return predicted_text

# 테스트
if __name__ == "__main__":
    time_ = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

    logger.add(f"result/t5_base/{time_}.log",format="{message}", level="INFO")
    gentext('공포, 모자, 빵', 64)