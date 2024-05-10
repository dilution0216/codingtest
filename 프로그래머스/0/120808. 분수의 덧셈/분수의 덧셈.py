from fractions import Fraction
#Fraction(분자,분모) 형식으로 사용한다.

def solution(numer1,denom1,numer2,denom2):
    result = Fraction(numer1,denom1)+Fraction(numer2,denom2)
    return (result.numerator, result.denominator)