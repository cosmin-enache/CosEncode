# CosEncode

An encoder I came up with while revising some python fundamentals

## How it works

### Encoder
The encoder takes a string ***s***, and generates pseudo-random integer key ***k***. 

Value of keys: **0** <= ***k*** < **len(***s*****)**

The encoder proceeds to add a pseudo-random, lower-case char ***c*** to string ***s*** at index ***k***

integer key ***k*** is appended to a list `rand_list`

This process happens recursively according to `max_no` and `times` and finishes when `max_no == times`

### Decoder
The decoder reverses the `rand_list`, loops through all the elements in the reversed list using index ***i***, and uses `list(s).pop(i)` to remove the random chars from the **encoded string**.
