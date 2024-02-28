obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}


def stringifyNumbers(obj):
    # TODO
    for k, v in obj.items():
        if isinstance(v, int):
            obj[k] = str(v)
        elif isinstance(v, dict):
            stringifyNumbers(obj[k])
    return obj

print (stringifyNumbers(obj))