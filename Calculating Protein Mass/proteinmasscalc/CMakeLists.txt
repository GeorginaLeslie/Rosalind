# cmake_minimum_required(VERSION <specify CMake version here>)
project(proteinmasscalc C)

set(CMAKE_C_STANDARD 11)

add_executable(proteinmasscalc main.c isotope_check.h isotope_check.c)