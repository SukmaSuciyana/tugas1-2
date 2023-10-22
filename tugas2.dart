
List<int> sequenceGenerator(int start, int stop) => 
    List<int>.generate(stop - start + 1, (i) => i + start);

List<dynamic> fizzBuzz(int a, int b) => 
    List<int>.generate(b - a, (i) => i + a).map((num) => 
        num % 15 == 0 ? 'FizzBuzz' :
        num % 3 == 0 ? 'Fizz' : 
        num % 5 == 0 ? 'Buzz' : num
    ).toList();

List<int> twoNumber(List<int> l) => 
    l.asMap().entries.where((e) => e.key < l.length - 1).map((e) => e.value + l[e.key + 1]).toList();

void main() {
  print(sequenceGenerator(1, 10));
  print(fizzBuzz(1, 20));
  print(twoNumber([1, 2, 3, 4]));
}

