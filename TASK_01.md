#Calculator_Application – Sample Test_Cases

## Test Case ID: TC_1
**Test Description:** Verify addition of two positive numbers.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 5
2. Press +
3. Enter 3
4. Press =
**Expected Result:** Display shows 8.

## Test Case ID: TC_2
**Test Description:** Verify subtraction of two positive numbers.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 9
2. Press -
3. Enter 4
4. Press =
**Expected Result:** Display shows 5.

## Test Case ID: TC_3
**Test Description:** Verify multiplication of two numbers.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 6
2. Press ×
3. Enter 7
4. Press =
**Expected Result:** Display shows 42.

## Test Case ID: TC_4
**Test Description:** Verify division of two numbers.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 8
2. Press ÷
3. Enter 2
4. Press =
**Expected Result:** Display shows 4.

## Test Case ID: TC_5
**Test Description:** Verify addition with negative numbers.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter -5
2. Press +
3. Enter 3
4. Press =
**Expected Result:** Display shows -2.

## Test Case ID: TC_6
**Test Description:** Verify decimal number calculation.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 2.5
2. Press ×
3. Enter 4
4. Press =
**Expected Result:** Display shows 10.

## Test Case ID: TC_7
**Test Description:** Verify BODMAS rule (operator precedence).  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 2 + 3 × 4
2. Press =
**Expected Result:** Display shows 14.

## Test Case ID: TC_8
**Test Description:** Verify mixed operator expression.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 10 - 2 × 3
2. Press =
**Expected Result:** Display shows 4.

## Test Case ID: TC_9
**Test Description:** Verify division by zero handling.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 10
2. Press ÷
3. Enter 0
4. Press =
**Expected Result:** Display shows error message (e.g., "Cannot divide by zero").

## Test Case ID: TC_10
**Test Description:** Verify non-numeric input handling.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 5 + a
2. Press =
**Expected Result:** Display shows invalid input error.

## Test Case ID: TC_11
**Test Description:** Verify special character handling.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 7 & 3
2. Press =
**Expected Result:** Display shows invalid input error.

## Test Case ID: TC_12
**Test Description:** Verify incomplete expression handling.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 8 +
2. Press =
**Expected Result:** Display shows error for incomplete expression.

## Test Case ID: TC_13
**Test Description:** Verify multiple operators together.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 5 ++ 2
2. Press =
**Expected Result:** Display shows invalid expression error.

## Test Case ID: TC_14
**Test Description:** Verify empty input handling.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Press =
**Expected Result:** Display shows no input or appropriate error message.

## Test Case ID: TC_15
**Test Description:** Verify large number calculation.  
**Preconditions:** Calculator is open.  
**Test Steps:**
1. Enter 999999 × 999999
2. Press =
**Expected Result:** Display shows correct calculated result.

