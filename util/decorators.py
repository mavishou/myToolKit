#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Created by Hou Mei on 2016/12/31

import wrapt


@wrapt.decorator
def print_func_name(func, instance, args, kwargs):
    print func.__name__
    ans = func(*args, **kwargs)
    return ans


@wrapt.decorator
def print_top_single_line(func, instance, args, kwargs):
    print '-'*50
    ans = func(*args, **kwargs)
    return ans


@wrapt.decorator
def print_bottom_single_line(func, instance, args, kwargs):
    ans = func(*args, **kwargs)
    print '-' * 50
    return ans


@wrapt.decorator
def print_both_single_line(func, instance, args, kwargs):
    print '-' * 50
    ans = func(*args, **kwargs)
    print '-' * 50
    return ans


@wrapt.decorator
def print_top_double_line(func, instance, args, kwargs):
    print '='*50
    ans = func(*args, **kwargs)
    return ans


@wrapt.decorator
def print_bottom_double_line(func, instance, args, kwargs):
    ans = func(*args, **kwargs)
    print '=' * 50
    return ans


@wrapt.decorator
def print_both_double_line(func, instance, args, kwargs):
    print '=' * 50
    ans = func(*args, **kwargs)
    print '=' * 50
    return ans