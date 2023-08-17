# Birth Year Calculator

This code is a command-line Python program that calculates the year(s) someone with a specific age was born. It uses the argparse module for parsing command-line arguments.

## Usage

```
python birthyear.py [options] year age
```

- `year` (integer): The current year or year of death.
- `age` (integer): The current age or age at death.

## Options

- `-c, --custom_name`: Optional. The person's name.
- `-x`: Optional. Display only one year (earliest).

## Example

```
python birthyear.py 2022 30
```

Output:

```
You were born between 1992 and 1993.
```

## Example with Custom Name

```
python birthyear.py 2022 30 -c John Doe
```

Output:

```
John Doe was born between 1992 and 1993.
```

## Example with Only One Year

```
python birthyear.py 2022 30 -x
```

Output:

```
You were born in 1992.
```

This is my first command-line Python program!
