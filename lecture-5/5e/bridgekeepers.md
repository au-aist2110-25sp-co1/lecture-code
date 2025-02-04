# A Tale of Two Bridgekeepers

## Nested Bridgekeeper

```
ask for name
if name is not correct
    throw off bridge
otherwise
    ask for quest
    if quest is not correct
        throw off bridge
    otherwise
        if sir robin
            ask for capital of asyria
            if capital is not correct
                throw off bridge
            otherwise
                allow to cross
        otherwise if galahad
            ask for favorite color
            if color is not correct
                throw off bridge
            otherwise
                allow to cross
        otherwise
            ask for airspeed velocity of swallow
            if velocity is not correct
                throw off bridge
            otherwise
                allow to cross
```

## Early Exit Bridgekeeper

```
ask for name
if name is not correct
    throw off bridge

ask for quest
if quest is not correct
    throw off bridge

if sir robin
    ask for capital of asyria
    if capital is not correct
        throw off bridge
otherwise if galahad
    ask for favorite color
    if color is not correct
        throw off bridge
otherwise
    ask for airspeed velocity of swallow
    if velocity is not correct
        throw off bridge

all tests passed so allow to cross
```
