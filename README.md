# BPE: Byte Pairing Encoding
![BPE](https://miro.medium.com/v2/resize:fit:1400/1*tQx4iDNDvME61PGO3t_qAw.png)

The original algorithm operates by iteratively replacing the most common contiguous sequences of characters in a target text with unused 'placeholder' bytes. The iteration ends when no sequences can be found, leaving the target text effectively compressed. Decompression can be performed by reversing this process, querying known placeholder terms against their corresponding denoted sequence, using a lookup table. In the original paper, this lookup table is encoded and stored alongside the compressed text.

Example
Suppose the data to be encoded is
```python
aaabdaaabac
```

The byte pair "aa" occurs most often, so it will be replaced by a byte that is not used in the data, such as "Z". Now there is the following data and replacement table:
```python
ZabdZabac
Z=aa
```
Then the process is repeated with byte pair "ab", replacing it with "Y":
```python
ZYdZYac
Y=ab
Z=aa
```
The only literal byte pair left occurs only once, and the encoding might stop here. Alternatively, the process could continue with recursive byte pair encoding, replacing "ZY" with "X":
```python
XdXac
X=ZY
Y=ab
Z=aa
```
This data cannot be compressed further by byte pair encoding because there are no pairs of bytes that occur more than once.

To decompress the data, simply perform the replacements in the reverse order.