# steempy-tools
support op: 
update_account、update_witness、withdraw、delegate_vest、vote_witness

## Quickstart

#### Installation
Prepare python3 environment and steem library.

``` 
pip3 install steem
```
 
#### Demo

For example, you need to vote a witness, just modify "config_vote_witness.json" in config directory, then run the command below.
  
```
[
  {
    "key": "",
    "vote_witness": {
      "account": "",
      "witness": "",
      "approve": true
    }
  }
]
```

```
python3 steem_ops.py vote_witness
```
