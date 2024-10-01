# Insertion Sort
### Umar's Variant

- Sequentially get a value from the list to compare (this is ```listToSort[i]```)
- Compare it with all values before it to find the earliest value which is greater
- If a previous value is greater than ```listToSort[i]``` (this will be ```listToSort[i2]```)
  - Store ```listToSort[i]``` in a buffer variable
  - Move all items between indexes ```i```(excl.) and ```i2```(incl.) one space to the right
  - Empty the buffer into the gap created at index ```i2```
  - Exit and start again for the next ```i```

## Visual Representation
![Demo](Demo.gif)