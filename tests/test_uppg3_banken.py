# 3 banken test
import pytest
from my_app.uppg3_banken import *


def test_deposit():
    # arrange
    deposit_amount = 100
    start_sum = 100
    expected_sum_after_deposit = start_sum + deposit_amount
    konto  = Bank_account("konto_deposit", start_sum)
    # act
    konto.deposit(deposit_amount)
    # assert
    assert konto.balance() == expected_sum_after_deposit


def test_withdraw():
    # arrange
    start_sum = 100
    withdraw_amount = 60
    expected_sum_after_withdraw = start_sum - withdraw_amount
    konto = Bank_account("konto_withdraw", start_sum)
    # act
    konto.withdraw(withdraw_amount)
    # assert
    assert konto.balance() == expected_sum_after_withdraw


def test_balance():
    # arrange
    start_sum = 100
    expected_balance = start_sum
    konto = Bank_account("konto_bal", start_sum)
    # act
    actual_balance = konto.balance()
    # assert
    assert expected_balance == actual_balance

def test_apply_interest():
    # arrange
    start_sum = 100
    interest = 0.10
    expected_balance_after_interest = start_sum * (1 +interest)
    konto = Bank_account("konto_apply", start_sum, interest)
    # act
    konto.apply_interest()
    actual_balance_after_interest = konto.balance()
    # assert
    assert actual_balance_after_interest == expected_balance_after_interest

def test_pay_a_bill_true():
    # arrange
    balance = 100
    bill = 66
    # bill < balance, betyder att räkningen kan betalas
    expected = True
    konto = Bank_account("konto_pay", 100)
    # act
    actual = konto.pay_a_bill(bill)
    # assert
    assert expected == actual