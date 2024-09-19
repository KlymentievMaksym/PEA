// Find the number of sentences in the given fragment of the text.
// Input
// Unique line contains the text fragment in English, the number of its symbols does not exceed 250. It is guaranteed that the text has no dash, hyphens, digits and numbers.
// Output
// Print the number of sentences in the text fragment.

// Examples
// Input #1
// Hello world!
// Answer #1
// 1
// Input #3
// Hi!!!
// Answer #3
// 1


#include <iostream>
using namespace std;

int main() 
{
    char text[250];
    cin.get(text, 250);
    
    int number_of_sentences = 0;
    char prev = ' ';
    for (char c : text) 
    {
        if (c == '.' || c == '!' || c == '?')
        {
            if (prev != '.' && prev != '!' && prev != '?')
            {
                number_of_sentences++;
            }
        }
        prev = c;
    }
    cout << number_of_sentences << endl;
}
