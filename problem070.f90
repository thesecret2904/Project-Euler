program problem070
    use iso_fortran_env, only: int32, int8, real64
    implicit none
    integer (int32) :: n, i, m, t
    real (real64) :: ratio, current
    integer (int32), allocatable :: primes(:)

    m = -1
    n = 9999999
    ! n = 100000
    ratio = huge(ratio)

    primes = get_primes(n)

    !$OMP PARALLEL DO PRIVATE(i, t, current)
    do i = 2, n
        ! write (*, '(I0, "/", I0, A)', advance="no") i, n, char(13)
        t = totient(i, primes)
        if ( are_permutations(i, t) ) then
            current = dble(i) / t
            !$OMP CRITICAL
            if ( current < ratio ) then
                m = i
                ratio = current
            end if
            !$OMP END CRITICAL
        end if
    end do
    !$OMP END PARALLEL DO

    print *, m

    contains

    integer(int32) function totient(n, primes)
        integer (int32), intent(in) :: n, primes(:)
        integer (int32) :: i, current, k, p
        integer (int32), allocatable :: factors(:)

        totient = 1
        i = 1
        current = n
        do while ( current > 1 )
            p = primes(i)
            k = 0

            do while( mod(current, p) == 0)
                k = k + 1
                current = current / p
            end do

            if ( k > 0 ) then
                totient = totient * p ** (k - 1) * (p - 1)
            end if

            i = i + 1
        end do
    end function totient

    elemental logical function are_permutations(a, b)
        integer (int32), intent(in) :: a, b
        integer (int32), dimension(10) :: a_count, b_count
        integer (int32) :: i, j
        ! max value of a is 2^32-1=4 294 967 295 which has 10 chars
        character(10) :: a_str, b_str

        a_count = 0
        b_count = 0

        write (a_str, '(I10)') a
        write (b_str, '(I10)') b
        do i = 1, 10
            if ( a_str(i:i) /= " " ) then
                read (a_str(i:i), *) j
                a_count(j + 1) = a_count(j + 1) + 1
            end if
            if ( b_str(i:i) /= " ") then
                read (b_str(i:i), *) j
                b_count(j + 1) = b_count(j + 1) + 1
            end if
        end do
        are_permutations = all(a_count == b_count)
    end function are_permutations

    function sieve_of_eratosthenes(limit) result(is_prime)
        integer (int32), intent(in) :: limit
        logical, allocatable, dimension(:) :: is_prime
        integer (int32) :: i, p

        allocate(is_prime(limit))
        is_prime = .true.

        is_prime(1) = .false.
        do i = 4, limit, 2
            is_prime(i) = .false.
        end do
        p = 3
        do while ( p * p <= limit )
            if ( is_prime(p) ) then
                do i = 2 * p, limit, p
                    is_prime(i) = .false.
                end do
            end if
            p = p + 2
        end do
    end function sieve_of_eratosthenes

    function get_primes(limit) result(primes)
        integer (int32), intent(in) :: limit
        integer (int32), allocatable, dimension(:) :: primes
        logical, allocatable, dimension(:) :: is_prime
        integer (int32) :: i, n_primes, prime

        is_prime = sieve_of_eratosthenes(limit)
        n_primes = count(is_prime)

        allocate(primes(n_primes))

        prime = 1
        do i = 1, limit
            if ( is_prime(i) ) then
                primes(prime) = i
                prime = prime + 1
            end if
        end do

    end function get_primes

    function get_multiplicity(n, m) result(k)
        integer (int32), intent(in) :: n, m
        integer (int32) :: k, r, c
        k = 0

        r = mod(n, m)
        c = n / m
        do while (r == 0)
            k = k + 1
            r = mod(c, m)
            c = c / m
        end do
    end function get_multiplicity

    function get_prime_factorization(n, primes) result(multiplicity)
        integer (int32), intent(in) :: n, primes(:)
        integer (int32), allocatable :: multiplicity(:)
        integer (int32) :: i, limit, j, k, m

        ! get the largest index such that  n <= p(limit)
        limit = binary_search(primes, n)

        allocate(multiplicity(limit))

        do i = 1, limit
            if ( mod(n, primes(i)) == 0 ) then
                multiplicity(i) = get_multiplicity(n, primes(i))
            else
                multiplicity(i) = 0
            end if
        end do
    end function get_prime_factorization

    pure function binary_search(arr, target) result(index)
        implicit none
        integer (int32), intent(in) :: arr(:)  ! Sorted array of real values
        integer (int32), intent(in) :: target  ! Target value to search for
        integer :: low, high, mid  ! Indices defining the search range
        integer :: index, n

        ! Initialize the result to 0 (indicating target not found)
        n = size(arr)
        low = 1
        high = n

        ! Perform binary search to find the correct insertion index
        do while (low <= high)
            mid = (low + high) / 2

            if (arr(mid) <= target .and. end_or_larger(arr, mid, target)) then
                ! Insert the target value after arr(mid)
                index = mid
                return
            elseif (arr(mid) < target) then
                ! Search in the right half of the array
                low = mid + 1
            else
                ! Search in the left half of the array
                high = mid - 1
            end if
        end do
        ! if the target value is less than all other values insert at the beginning
        index = 1
    end function binary_search

    pure logical function end_or_larger(arr, mid, target)
        integer (int32), intent(in) :: arr(:), target
        integer, intent(in) :: mid

        if ( mid == size(arr) ) then
           end_or_larger = .true.
        else if (arr(mid + 1) > target) then
           end_or_larger = .true.
        else
           end_or_larger = .false.
        end if
    end function end_or_larger

end program problem070