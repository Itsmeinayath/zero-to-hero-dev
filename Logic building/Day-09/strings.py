"""strings.py – Day 9 Playground (Strings)
Goal: Consolidated, runnable reference for core string concepts + common algorithms.

Sections:
 1. Fundamentals & immutability
 2. Core operations & methods (with complexity notes)
 3. Efficient building vs naive concatenation
 4. Mini algorithms (reverse, palindrome, anagram, vowel count, first unique char)
 5. Utility demonstrations (escape sequences, formatting)
 6. Quick self‑tests / assertions

Run: python strings.py
"""

from __future__ import annotations
from collections import Counter
from typing import Dict, List, Optional

LINE = "-" * 60

# 1. Fundamentals -----------------------------------------------------------
def fundamentals_demo() -> None:
	print(LINE)
	print("1) Fundamentals & Immutability")
	s = "john doe"
	print("Original:", s)
	# Attempting mutation would raise: TypeError: 'str' object does not support item assignment
	# Instead create new strings:
	capitalized = s.title()  # O(n)
	print("Title():", capitalized)
	sliced = s[0:4]  # 'john'
	print("Slice [0:4]:", sliced)
	reversed_copy = s[::-1]  # new reversed string O(n) time & space
	print("Reversed copy (s[::-1]):", reversed_copy)
	print("Length O(1):", len(s))


# 2. Core operations / methods ---------------------------------------------
def core_methods_demo() -> None:
	print(LINE)
	print("2) Core Methods & Operations")
	first_name, last_name = "john", "doe"
	full_name = first_name + " " + last_name  # concatenation builds new string
	print("Full name:", full_name)
	print("Index [0]:", full_name[0])  # O(1)
	print("Index [-1]:", full_name[-1])  # O(1)
	# Every method below returns a NEW string (original unchanged) except find/count/startswith/endswith which return numbers/bools.
	print("lower():", full_name.lower(), "-> lowercases (Unicode aware, simple) O(n)")
	print("upper():", full_name.upper(), "-> uppercases O(n)")
	print("strip():", "   John Doe   ".strip(), "-> trims ends only O(n)")
	print("replace():", full_name.replace("john", "joy"), "-> substitutes all (unless count given) O(n)")
	print("split(' '):", full_name.split(" "), "-> splits on delimiter, returns list O(n)")
	print("' '.join([...]):", " ".join(["john", "doe"]), "-> efficient assembly O(total)")
	print("find('john'):", full_name.find("john"), "-> first index or -1 O(n*m) worst")
	print("count('o'):", full_name.count("o"), "-> frequency scan O(n)")
	print("startswith('john'):", full_name.startswith("john"), "-> prefix test O(k)")
	print("endswith('doe'):", full_name.endswith("doe"), "-> suffix test O(k)")
	print("casefold():", full_name.casefold(), "-> aggressive lowercase for comparisons (e.g., German ß)")


def method_reference() -> None:
	"""Detailed human-readable explanations (quick doc style)."""
	print(LINE)
	print("2a) Method Explanations")
	explanations = [
		("lower()", "Return new string with all cased characters converted to lowercase. Use for normalization before comparisons. 'JOhn' -> 'john'."),
		("casefold()", "Stronger lowercase intended for caseless matching (handles ß → ss). Prefer for international text matching."),
		("upper()", "Return new string with all cased characters uppercase."),
		("strip()/lstrip()/rstrip()", "Remove whitespace (or provided chars) from both/left/right ends. Does NOT touch interior spaces."),
		("replace(old, new, count?)", "Return new string replacing occurrences of old with new. If count omitted, replaces all. Scans left→right."),
		("split(sep)", "Split into list. If sep omitted, collapses consecutive whitespace. If sep provided, empty fields preserved (e.g., 'a,,b'.split(',') -> ['a', '', 'b'])."),
		("join(iterable)", "Opposite of split: Efficiently concatenates iterable of strings using current string as separator. Preferred over += loops."),
		("find(sub)", "Return lowest index of sub or -1. Use index() if you want ValueError on absence."),
		("count(sub)", "Non-overlapping occurrences count. For overlaps you need manual scan (e.g., 'aaa'.count('aa') == 1, not 2)."),
		("startswith(prefix)/endswith(suffix)", "Boolean prefix/suffix test; can pass tuple of candidates. Optional start/end slice arguments."),
		("in operator", "'sub' in s performs substring search; returns bool. Complexity O(n*m) naive."),
		("s[::-1]", "Slice trick to reverse; creates new string. O(n) time & space."),
	]
	for name, explanation in explanations:
		print(f"- {name}: {explanation}")
	print("Pitfalls:")
	print("  * Repeated += concatenation in loops -> O(n^2) growth")
	print("  * strip() only removes ends, not internal whitespace")
	print("  * count() non-overlapping: 'aaaa'.count('aa') == 2")
	print("  * casefold() vs lower(): use casefold for robust locale-insensitive comparisons")


# 3. Efficient building -----------------------------------------------------
def inefficient_concat(n: int) -> str:
	"""Anti-pattern: O(n^2) due to repeated reallocation."""
	result = ""
	for i in range(n):
		result += str(i)  # each step copies
	return result


def efficient_build(n: int) -> str:
	"""Preferred: collect then join O(n)."""
	parts = []
	for i in range(n):
		parts.append(str(i))
	return "".join(parts)


def building_demo() -> None:
	print(LINE)
	print("3) Building Strings Efficiently (tiny scale illustration)")
	print("inefficient_concat(5):", inefficient_concat(5))
	print("efficient_build(5):  ", efficient_build(5))
	# (For large n you'd benchmark; omitted to keep runtime fast.)


# 4. Mini algorithms --------------------------------------------------------
def reverse_in_place(chars: List[str]) -> None:
	"""Reverse list of characters in-place. O(n) time / O(1) space."""
	l, r = 0, len(chars) - 1
	while l < r:
		chars[l], chars[r] = chars[r], chars[l]
		l += 1
		r -= 1


def reversed_copy(s: str) -> str:
	return s[::-1]  # new string


def is_palindrome(s: str) -> bool:
	i, j = 0, len(s) - 1
	while i < j:
		while i < j and not s[i].isalnum():
			i += 1
		while i < j and not s[j].isalnum():
			j -= 1
		if s[i].lower() != s[j].lower():
			return False
		i += 1
		j -= 1
	return True


def are_anagrams(a: str, b: str) -> bool:
	"""Check anagrams by counting frequency. O(n) time / O(1) space (alphabet bounded)."""
	if len(a) != len(b):
		return False
	freq = Counter(a)
	for ch in b:
		if ch not in freq:
			return False
		freq[ch] -= 1
		if freq[ch] == 0:
			del freq[ch]
	return not freq


def vowel_count(s: str) -> Dict[str, int]:
	vowels = set("aeiouAEIOU")
	counts: Dict[str, int] = {}
	for ch in s:
		if ch in vowels:
			counts[ch.lower()] = counts.get(ch.lower(), 0) + 1
	return counts


def first_unique_char(s: str) -> Optional[int]:
	"""Return index of first non-repeating character or None. O(n)."""
	freq = Counter(s)
	for i, ch in enumerate(s):
		if freq[ch] == 1:
			return i
	return None


def algorithms_demo() -> None:
	print(LINE)
	print("4) Algorithms")
	# Reverse list
	chars = list("hello")
	reverse_in_place(chars)
	print("reverse_in_place('hello') ->", ''.join(chars))
	print("reversed_copy('world') ->", reversed_copy("world"))
	print("is_palindrome('A man, a plan, a canal: Panama') ->", is_palindrome("A man, a plan, a canal: Panama"))
	print("is_palindrome('race a car') ->", is_palindrome("race a car"))
	print("are_anagrams('listen','silent') ->", are_anagrams("listen", "silent"))
	print("are_anagrams('apple','papel') ->", are_anagrams("apple", "papel"))
	print("are_anagrams('rat','car') ->", are_anagrams("rat", "car"))
	print("vowel_count('Beautiful day') ->", vowel_count("Beautiful day"))
	print("first_unique_char('leetcode') -> index", first_unique_char("leetcode"))
	print("first_unique_char('aabb') ->", first_unique_char("aabb"))


# 5. Formatting & escape sequences -----------------------------------------
def formatting_demo() -> None:
	print(LINE)
	print("5) Formatting & Escapes")
	full_name = "john doe"
	age = 30
	print(f"f-string: {full_name} is {age} years old.")
	print("format(): {} is {} years old.".format(full_name, age))
	print("Escapes:")
	print("He said, \"Hello, World!\"")
	print('It\'s a beautiful day.')
	print("C:\\Users\\JohnDoe")
	print("First Line\nSecond Line")
	print("Column1\tColumn2\tColumn3")


# 6. Quick assertions (mini self-test) -------------------------------------
def self_tests() -> None:
	print(LINE)
	print("6) Self-tests (assertions)")
	assert reversed_copy("") == ""
	assert reversed_copy("a") == "a"
	c = list("ab")
	reverse_in_place(c)
	assert ''.join(c) == "ba"
	assert is_palindrome("") is True
	assert is_palindrome("0P") is False
	assert are_anagrams("abc", "cab") is True
	assert are_anagrams("abc", "ab") is False
	assert first_unique_char("leetcode") == 0
	assert first_unique_char("aabbccdde") == 8
	print("All basic assertions passed ✅")


def summary() -> None:
	print(LINE)
	print("SUMMARY")
	print("Immutability -> create new strings; use lists for in-place style work")
	print("Avoid O(n^2) concatenation; prefer join()")
	print("Two-pointer patterns: reverse, palindrome")
	print("Frequency counting (Counter / dict) unlocks anagram & uniqueness checks")
	print("Always annotate complexity mentally: slice O(k), join O(total), membership O(n)")


def main() -> None:
	fundamentals_demo()
	core_methods_demo()
	method_reference()
	building_demo()
	algorithms_demo()
	formatting_demo()
	self_tests()
	summary()


if __name__ == "__main__":  # pragma: no cover
	main()

