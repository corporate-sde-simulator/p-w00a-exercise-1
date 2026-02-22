"""
Tests for Exercise 1: Python Fundamentals
Run with: python -m pytest test_exercise.py -v
"""
import pytest
import threading
import logging
from starter import (
    create_variables,
    rectangle_area,
    calculate_total,
    find_largest,
    filter_evens,
    create_student,
    merge_dicts,
    TaskList,
    safe_int,
    safe_get,
    format_receipt,
    transform_words,
    extract_fields,
    merge_json_configs,
    ThreadSafeCounter,
    process_records,
    retry,
    extract_ips,
    parse_log_line,
    call_module_function,
)


# ─── Part 1: Variables ─────────────────────────────────────────────
class TestVariables:
    def test_create_variables_returns_four_values(self):
        result = create_variables()
        assert result is not None, "create_variables() should return something, not None"
        assert len(result) == 4, "Should return exactly 4 values: name, age, gpa, is_enrolled"

    def test_create_variables_types(self):
        name, age, gpa, is_enrolled = create_variables()
        assert isinstance(name, str), f"name should be a string, got {type(name).__name__}"
        assert isinstance(age, int), f"age should be an integer, got {type(age).__name__}"
        assert isinstance(gpa, float), f"gpa should be a float, got {type(gpa).__name__}"
        assert isinstance(is_enrolled, bool), f"is_enrolled should be a boolean, got {type(is_enrolled).__name__}"


# ─── Part 2: Functions ────────────────────────────────────────────
class TestFunctions:
    def test_rectangle_area_basic(self):
        assert rectangle_area(5, 3) == 15, "5 × 3 should be 15"

    def test_rectangle_area_square(self):
        assert rectangle_area(4, 4) == 16, "4 × 4 should be 16"

    def test_rectangle_area_float(self):
        assert rectangle_area(2.5, 4) == 10.0, "2.5 × 4 should be 10.0"

    def test_calculate_total_default_tax(self):
        result = calculate_total(100)
        assert result == 110.0, "100 with default 10% tax should be 110.0"

    def test_calculate_total_custom_tax(self):
        result = calculate_total(100, 0.2)
        assert result == 120.0, "100 with 20% tax should be 120.0"

    def test_calculate_total_zero_tax(self):
        result = calculate_total(50, 0)
        assert result == 50.0, "50 with 0% tax should be 50.0"


# ─── Part 3: Lists ────────────────────────────────────────────────
class TestLists:
    def test_find_largest_basic(self):
        assert find_largest([3, 7, 2, 9, 4]) == 9

    def test_find_largest_single(self):
        assert find_largest([5]) == 5

    def test_find_largest_negative(self):
        assert find_largest([-1, -5, -2]) == -1

    def test_find_largest_all_same(self):
        assert find_largest([3, 3, 3]) == 3

    def test_filter_evens_basic(self):
        assert filter_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_filter_evens_no_evens(self):
        assert filter_evens([1, 3, 5]) == []

    def test_filter_evens_all_evens(self):
        assert filter_evens([2, 4, 6]) == [2, 4, 6]

    def test_filter_evens_with_zero(self):
        assert filter_evens([0, 1, 2]) == [0, 2]


# ─── Part 4: Dictionaries ─────────────────────────────────────────
class TestDictionaries:
    def test_create_student_basic(self):
        result = create_student("Alice", 20, [85, 90, 78])
        assert result["name"] == "Alice"
        assert result["age"] == 20
        assert result["grades"] == [85, 90, 78]
        assert round(result["average"], 2) == 84.33

    def test_create_student_single_grade(self):
        result = create_student("Bob", 22, [100])
        assert result["average"] == 100.0

    def test_merge_dicts_basic(self):
        result = merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
        assert result == {"a": 1, "b": 3, "c": 4}

    def test_merge_dicts_no_overlap(self):
        result = merge_dicts({"a": 1}, {"b": 2})
        assert result == {"a": 1, "b": 2}

    def test_merge_dicts_empty(self):
        result = merge_dicts({}, {"a": 1})
        assert result == {"a": 1}


# ─── Part 5: Classes ──────────────────────────────────────────────
class TestTaskList:
    def test_add_task(self):
        tl = TaskList()
        tl.add_task("Buy milk")
        assert len(tl.tasks) == 1
        assert tl.tasks[0]["name"] == "Buy milk"
        assert tl.tasks[0]["done"] == False

    def test_complete_task(self):
        tl = TaskList()
        tl.add_task("Buy milk")
        tl.complete_task("Buy milk")
        assert tl.tasks[0]["done"] == True

    def test_complete_nonexistent_task(self):
        tl = TaskList()
        tl.add_task("Buy milk")
        tl.complete_task("Fly to moon")  # Should not crash
        assert tl.tasks[0]["done"] == False

    def test_get_pending(self):
        tl = TaskList()
        tl.add_task("Buy milk")
        tl.add_task("Write code")
        tl.add_task("Read book")
        tl.complete_task("Buy milk")
        pending = tl.get_pending()
        assert "Write code" in pending
        assert "Read book" in pending
        assert "Buy milk" not in pending

    def test_get_pending_empty(self):
        tl = TaskList()
        assert tl.get_pending() == []


# ─── Part 6: Error Handling ───────────────────────────────────────
class TestErrorHandling:
    def test_safe_int_valid(self):
        assert safe_int("42") == 42

    def test_safe_int_invalid(self):
        assert safe_int("hello") == 0

    def test_safe_int_custom_default(self):
        assert safe_int("xyz", -1) == -1

    def test_safe_int_float_string(self):
        assert safe_int("3.14") == 0

    def test_safe_get_nested(self):
        data = {"a": {"b": {"c": 42}}}
        assert safe_get(data, ["a", "b", "c"]) == 42

    def test_safe_get_missing_key(self):
        data = {"a": {"b": 1}}
        assert safe_get(data, ["a", "x", "y"]) is None

    def test_safe_get_single_key(self):
        data = {"a": 1}
        assert safe_get(data, ["a"]) == 1

    def test_safe_get_empty_keys(self):
        data = {"a": 1}
        assert safe_get(data, []) == data


# ─── Part 7: String Formatting ────────────────────────────────────
class TestFormatting:
    def test_format_receipt_basic(self):
        items = [
            {"name": "Coffee", "price": 4.50},
            {"name": "Muffin", "price": 3.25},
        ]
        result = format_receipt(items)
        assert "Coffee" in result
        assert "Muffin" in result
        assert "$4.50" in result
        assert "$3.25" in result
        assert "$7.75" in result
        assert "Total" in result

    def test_format_receipt_single_item(self):
        items = [{"name": "Tea", "price": 2.00}]
        result = format_receipt(items)
        assert "Tea" in result
        assert "$2.00" in result
        assert "Total" in result


# ─── Part 8: List Comprehensions ──────────────────────────────────
class TestComprehensions:
    def test_transform_words_basic(self):
        result = transform_words(["hi", "hello", "hey", "python", "go"])
        assert result == ["HELLO", "PYTHON"]

    def test_transform_words_all_short(self):
        result = transform_words(["hi", "go", "at"])
        assert result == []

    def test_transform_words_all_long(self):
        result = transform_words(["hello", "world", "python"])
        assert result == ["HELLO", "WORLD", "PYTHON"]


# ─── Part 9: File I/O & JSON ─────────────────────────────────────
class TestJSON:
    def test_extract_fields_basic(self):
        result = extract_fields('{"name": "Alice", "age": 25, "city": "NYC"}', ["name", "age"])
        assert result == {"name": "Alice", "age": 25}

    def test_extract_fields_missing(self):
        result = extract_fields('{"a": 1}', ["a", "b"])
        assert result == {"a": 1}

    def test_extract_fields_all_missing(self):
        result = extract_fields('{"a": 1}', ["x", "y"])
        assert result == {}

    def test_merge_json_configs(self):
        result = merge_json_configs([
            '{"host": "localhost", "port": 3000}',
            '{"port": 8080, "debug": true}'
        ])
        assert result == {"host": "localhost", "port": 8080, "debug": True}

    def test_merge_json_configs_three_layers(self):
        result = merge_json_configs([
            '{"a": 1, "b": 2}',
            '{"b": 3, "c": 4}',
            '{"c": 5}'
        ])
        assert result == {"a": 1, "b": 3, "c": 5}


# ─── Part 10: Threading ──────────────────────────────────────────
class TestThreading:
    def test_counter_basic(self):
        c = ThreadSafeCounter()
        c.increment()
        c.increment()
        assert c.get_count() == 2

    def test_counter_decrement(self):
        c = ThreadSafeCounter()
        c.increment()
        c.increment()
        c.increment()
        c.decrement()
        assert c.get_count() == 2

    def test_counter_threaded(self):
        """This test proves thread safety — without locks it WILL fail!"""
        c = ThreadSafeCounter()
        threads = []
        for _ in range(100):
            t = threading.Thread(target=c.increment)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        assert c.get_count() == 100, "100 threads incrementing should give 100"


# ─── Part 11: Logging ────────────────────────────────────────────
class TestLogging:
    def test_process_records_count(self):
        records = [
            {"id": 1, "status": "ok", "message": "fine"},
            {"id": 2, "status": "error", "message": "disk full"},
            {"id": 3, "message": "no status"},
        ]
        assert process_records(records) == 1

    def test_process_records_all_ok(self):
        records = [
            {"id": 1, "status": "ok"},
            {"id": 2, "status": "ok"},
        ]
        assert process_records(records) == 2

    def test_process_records_empty(self):
        assert process_records([]) == 0


# ─── Part 12: Decorators ─────────────────────────────────────────
class TestDecorators:
    def test_retry_succeeds_first_try(self):
        @retry(max_retries=3)
        def always_works():
            return 42
        assert always_works() == 42

    def test_retry_succeeds_after_failures(self):
        attempt = {"count": 0}

        @retry(max_retries=3)
        def fails_twice():
            attempt["count"] += 1
            if attempt["count"] < 3:
                raise ValueError("Not yet!")
            return "success"
        assert fails_twice() == "success"

    def test_retry_all_fail(self):
        @retry(max_retries=2)
        def always_fails():
            raise RuntimeError("Broken")
        with pytest.raises(RuntimeError):
            always_fails()


# ─── Part 13: Regex ──────────────────────────────────────────────
class TestRegex:
    def test_extract_ips_basic(self):
        result = extract_ips("Connection from 192.168.1.1 and 10.0.0.5 failed")
        assert result == ["192.168.1.1", "10.0.0.5"]

    def test_extract_ips_none(self):
        assert extract_ips("No IPs here") == []

    def test_extract_ips_single(self):
        result = extract_ips("Server at 127.0.0.1")
        assert result == ["127.0.0.1"]

    def test_parse_log_line_valid(self):
        result = parse_log_line("[2026-01-15 14:30:00] ERROR: Connection timeout")
        assert result["timestamp"] == "2026-01-15 14:30:00"
        assert result["level"] == "ERROR"
        assert result["message"] == "Connection timeout"

    def test_parse_log_line_invalid(self):
        assert parse_log_line("not a log line") is None


# ─── Part 14: Imports & Multi-File ───────────────────────────────
class TestModules:
    def test_call_module_function(self):
        mod = {"add": lambda a, b: a + b, "multiply": lambda a, b: a * b}
        assert call_module_function(mod, "add", 3, 5) == 8

    def test_call_module_function_multiply(self):
        mod = {"add": lambda a, b: a + b, "multiply": lambda a, b: a * b}
        assert call_module_function(mod, "multiply", 4, 5) == 20

    def test_call_module_function_unknown(self):
        mod = {"add": lambda a, b: a + b}
        assert call_module_function(mod, "unknown", 1, 2) is None
