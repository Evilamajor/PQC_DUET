# RSA Summary

RSA encryption is a public-key cryptographic system built on the properties of finite fields, number theory, and Euler’s theorem.

The system begins by selecting two large prime numbers \( p \) and \( q \), used to compute \( n = p \cdot q \) and Euler’s totient function \( \varphi(n) = (p - 1)(q - 1) \). A public exponent \( e \) is chosen such that \( \gcd(e, \varphi(n)) = 1 \), ensuring the existence of a modular inverse \( d \), computed via the extended Euclidean algorithm.

The public key consists of \( (n, e) \) and is used to encrypt messages using:

\[
c \equiv m^e \mod n
\]

The private key \( d \) allows the original message to be recovered using:

\[
m \equiv c^d \mod n
\]

The correctness of decryption is guaranteed by Euler’s theorem, which states that for any \( m \) coprime with \( n \):

\[
m^{\varphi(n)} \equiv 1 \mod n
\]

This implies:

\[
m^{ed} \equiv m \mod n
\]

when \( ed \equiv 1 \mod \varphi(n) \).

RSA security relies on the hardness of factoring large integers. Its elegance lies in combining elementary mathematical tools (primes, GCD, inverses, modular arithmetic) into a robust encryption protocol.



