# Solidity Generator 
This server application presents an inference endpoint for code generation purposes.

# Download the solidity generator model
The pretrained model can be found [here](https://huggingface.co/ckandemir/solidity-generator)

```bash
git lfs install
git clone https://huggingface.co/ckandemir/solidity-generator
```

## Build the server app 
```bash
docker-compose up --build
```

## Test the app
```bash
python test.py
```