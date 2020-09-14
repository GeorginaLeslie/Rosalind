cmake_minimum_required(VERSION 3.15)
project(Finding_a_Motif_in_DNA C)

set(CMAKE_C_STANDARD 11)

add_executable(Finding_a_Motif_in_DNA main.c motif_finder.c motif_finder.h modulo.c modulo.h)