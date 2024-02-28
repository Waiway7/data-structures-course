
obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

def collectStrings(obj):
    # TODO
    arr = []
    for k, v in obj.items():
        if type(v) is str:
            arr.append(v)
        elif type(v) is dict:
            arr.extend(collectStrings(obj[k]))
    return arr

print (collectStrings(obj))