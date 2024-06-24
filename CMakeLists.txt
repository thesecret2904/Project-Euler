cmake_minimum_required(VERSION 3.26)
project(ProjectEuler VERSION 1.0.0)

enable_language(Fortran)

find_package(OpenMP REQUIRED)
# Check if the build type is Debug and the compiler is gfortran
if(CMAKE_Fortran_COMPILER_ID STREQUAL "GNU")
        message(STATUS "Configuring flags for gfortran")
        if(CMAKE_BUILD_TYPE STREQUAL "Debug")
            set(CMAKE_Fortran_FLAGS "-g -O0 -Wall -fcheck=all -fbacktrace -fbounds-check")
        elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
            set(CMAKE_Fortran_FLAGS "-O3 -march=native -funroll-loops")
        endif()
elseif(CMAKE_Fortran_COMPILER_ID STREQUAL "Intel" OR CMAKE_Fortran_COMPILER_ID STREQUAL "IntelLLVM")
        message(STATUS "Configuring flags for Intel Fortran")
        if(CMAKE_BUILD_TYPE STREQUAL "Debug")
            set(CMAKE_Fortran_FLAGS "-g -O0 -warn all -check all -traceback")
        elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
            set(CMAKE_Fortran_FLAGS "-Ofast -xHost -funroll-loops")
        elseif(CMAKE_BUILD_TYPE STREQUAL "Profile")
            set(CMAKE_Fortran_FLAGS "-Ofast -xHost -funroll-loops -g")
        endif()
endif()

message(STATUS "Flags: ${CMAKE_Fortran_FLAGS}")
set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} ${OpenMP_Fortran_FLAGS}")

add_executable(problem070 problem070.f90)