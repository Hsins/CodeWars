# Remove String Spaces

## Information

- KYU: 8
- Link: [Remove String Spaces](https://www.codewars.com/kata/remove-string-spaces/train/shell)

## Description:

Simple, remove the spaces from the string, then return the resultant string.

## My Solution

```shell
echo "$1" | tr -d " "
```

## Clever Solutions

```shell
echo ${1// /}
```

```shell
echo "${1// }"
```

```shell
echo $1 | sed -s 's/ //g'
```

```shell
echo $(tr -d ' ' <<<$1)
```

## References

- [stackoverflow | How do I remove spaces from shell variables?](https://unix.stackexchange.com/questions/156579/how-do-i-remove-spaces-from-shell-variables)