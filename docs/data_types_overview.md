# CPS 141 - Python Data Types Overview
**Washtenaw Community College**

> This guide explains the most common Python data types using University of Michigan themed examples.
> The goal is simple: understand what kind of value you are storing, and why that type matters.

---

## What Is a Data Type?

A **data type** tells Python what kind of value a variable holds.

Examples:
- a whole number
- a decimal number
- text
- true/false
- a group of values

When you choose the right data type, your program becomes easier to read, easier to fix, and easier to extend.

---

## 1. Integer (`int`)

An integer is a **whole number** with no decimal part.

```python
touchdowns = 5
basketball_players_on_court = 5
jersey_number = 23
```

Use an integer when you are counting things:
- points scored in a quarter
- number of rebounds
- number of students in a class

Why it fits:
- `5` touchdowns is a count, not text
- jersey numbers are usually stored as whole numbers

---

## 2. Float (`float`)

A float is a **number with a decimal**.

```python
three_point_percentage = 38.7
gpa = 3.82
forty_yard_dash_time = 4.56
```

Use a float when the value can include fractions or decimals.

Why it fits:
- shooting percentages often include decimals
- race times are rarely whole numbers

---

## 3. String (`str`)

A string is **text**. Strings go inside quotes.

```python
team_name = "Michigan Wolverines"
stadium = "Michigan Stadium"
fight_song = "The Victors"
```

Use a string for:
- names
- messages
- labels
- course titles

Why it fits:
- `"Michigan Wolverines"` is text, not a number

---

## 4. Boolean (`bool`)

A boolean stores only one of two values:
- `True`
- `False`

```python
won_the_game = True
is_home_game = False
assignment_submitted = True
```

Use a boolean when the answer is yes/no, on/off, or true/false.

Why it fits:
- either the team won or it did not
- either the assignment was submitted or it was not

---

## 5. List (`list`)

A list stores **multiple values in order**.

Lists use square brackets: `[]`

```python
basketball_scores = [78, 82, 91, 88]
captains = ["Dylan", "Jordan", "Maya"]
home_opponents = ["Ohio State", "Michigan State", "Penn State"]
```

Use a list when:
- order matters
- you may add or remove items
- you want to loop through values

Why it fits:
- game scores can be stored in sequence
- a schedule is usually kept in order

---

## 6. Tuple (`tuple`)

A tuple is like a list, but it is usually used for a **fixed group of related values**.

Tuples use parentheses: `()`

```python
final_score = (31, 24)
player_height = (6, 2)
school_colors = ("maize", "blue")
```

Use a tuple when the values belong together and should not change often.

Why it fits:
- a final score is one pair of related numbers
- school colors are a fixed pair

---

## 7. Dictionary (`dict`)

A dictionary stores **key-value pairs**.

Dictionaries use curly braces: `{}`

```python
quarterback_stats = {
    "name": "J.J. McCarthy",
    "touchdowns": 3,
    "interceptions": 0,
    "completion_rate": 72.4
}
```

Use a dictionary when you want to label each value.

Why it fits:
- stats make more sense when each number has a name
- `"touchdowns": 3` is clearer than just storing `3` by itself

---

## 8. Set (`set`)

A set stores **unique values only**.

```python
rival_teams = {"Ohio State", "Michigan State", "Notre Dame"}
```

Use a set when:
- duplicates should not exist
- you only care whether an item is present

Why it fits:
- a rival should only appear once in the collection

---

## 9. None (`NoneType`)

`None` means **no value has been assigned yet**.

```python
starting_quarterback = None
final_grade = None
```

Use `None` when:
- the value is unknown right now
- you plan to fill it in later

Why it fits:
- before the coach announces a starter, the value may be unknown

---

## Quick Comparison

| Type | Example | Best For |
|------|---------|----------|
| `int` | `7` | counts, whole numbers |
| `float` | `42.5` | decimals, measurements |
| `str` | `"Go Blue"` | text |
| `bool` | `True` | yes/no decisions |
| `list` | `["Iowa", "Indiana", "Minnesota"]` | ordered collections |
| `tuple` | `(27, 20)` | fixed grouped values |
| `dict` | `{"points": 24, "rebounds": 11}` | labeled data |
| `set` | `{"maize", "blue"}` | unique values |
| `None` | `None` | missing or not-yet-known data |

---

## Why Data Types Matter

Python treats different types differently.

```python
points = 30
message = "30"
```

These may look similar, but they are not the same:
- `points` is a number
- `message` is text

That changes what Python lets you do.

```python
print(points + 5)      # 35
print(message + "5")   # 305
```

This is one of the biggest beginner lessons in programming:
the value is not just what you see, it is also how Python understands it.

---

## Example Program

```python
team_name = "Michigan Wolverines"
wins = 15
win_percentage = 93.8
made_playoffs = True
team_captains = ["Dylan", "Avery", "Mason"]
record = {"wins": 15, "losses": 1}

print(team_name)
print(wins)
print(win_percentage)
print(made_playoffs)
print(team_captains)
print(record)
```

This short example uses several data types in one program:
- string for the team name
- integer for wins
- float for percentage
- boolean for playoff status
- list for captains
- dictionary for the record

---

## Questions to Ask Yourself

When choosing a data type, ask:

1. Is this a number, text, or true/false value?
2. Do I need one value or many values?
3. If I need many values, do I need labels?
4. Does order matter?
5. Can duplicates exist?

These questions usually point you to the right type.

---

## Practice Ideas

Try creating variables for:

1. The number of points Michigan scored in a football game
2. The name of the basketball arena
3. Whether Dylan finished Assignment 1
4. A list of Michigan opponents
5. A dictionary of player stats

Then use `print(type(variable_name))` to check each one.

```python
team = "Michigan"
print(type(team))
```

---

## Final Takeaway

A data type is not just a technical detail. It is part of how you describe the real world in code.

If you can look at a value and say:
- this is text
- this is a count
- this is a decimal
- this is a list of items
- this is labeled information

then you are thinking like a programmer.

---

*CPS 141 | Data Types Reference | Go Blue!*
