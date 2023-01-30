// Using the new class
#include "MyClass.h"

#include <iostream>
#include <stdio.h>

int main( /*int argc, char * argv[]*/ )
{
  // Create an instance of the class – just as we might have a variable that is an int, here we have a MyClass
  MyClass anInstance( 17 );

  // Run the method of MyClass and print the result
  int result = anInstance.TestMethod( 13 );
  std::cout << "The result was " << result << std::endl;

  // for loop that prints the numbers 0 to 9
  for ( int i = 0; i < 10; i++ )
  {
    cout << i << endl;
  };
}
