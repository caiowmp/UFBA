# Equipe (nomes)

# Código para a questão 1

use strict;
use warnings;

# escopo estático
my $op1 = 4;
my $op2 = 10;

sub soma()
{
  my $sum = $op1 + $op2;
  return $sum;
}

print soma();

#escopo dinâmico

sub somaDinamica(){
    $op1 = 10;
    $op2 = 20;
    return soma()
}
print "\n";
print somaDinamica();
print "\n";