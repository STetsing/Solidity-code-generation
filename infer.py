import json
import time
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('./solidity-generator/', trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained('./solidity-generator/', trust_remote_code=True)

def infer(data):
    data = json.loads(data)
    msg = data['prefix']
    mxl = data['max_token']
    start = time.time()
    x = tokenizer.encode(msg, return_tensors='pt')
    y = model.generate(x, max_length=mxl, do_sample=True, top_p=0.95, top_k=4, temperature=0.2, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)
    generated_code = tokenizer.decode(y[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
    # print('#'*100)
    # print(generated_code)
    # print('#'*100)
    # end = time.time()
    # print('time used:', end - start, 'seconds')

    return json.dumps(generated_code)
