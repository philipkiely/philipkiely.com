##About Shakespearean Rhymes
###Rhyme a word
This program, when given one of over 1,000 unique words, returns a line of iambic pentameter that rhymes with the given word. The program uses all 152 of Shakespeare's complete sonnets to generate these lines, as sonnets have a strict meter and rhyme scheme. The sonnets, as part of the public domain, are available at [https://www.opensourceshakespeare.org/views/sonnets/sonnets.php](opensourceshakespeare.org)

The program has two arrays that hold the data: "sonnets" and "end_rhymes". The "sonnets" array holds each sonnet as an array of fourteen strings, while the "end_rhymes" array holds the last word of each line of each sonnet. First, the program takes the given word and runs it through the "end_rhymes" array to find the index of the word. This is the same index as the corresponding sonnet in the "sonnets" array. From there, the program uses a series of loops to determine the correct line to rhyme with, given the sonnet's strictly defined rhyme scheme. It proudly displays this rhyming line.

###Create a sonnet
Using the same data as the word-rhyming program, this program generates an entire sonnet by combining existing lines of Shakespeare's poetry. Using the rhyming line program, it creates poems where the lines that rhyme are not necessarily from the same poem.

The program takes seven random words from the "end_rhymes" array and matches rhyming lines. It then matches the last word of each of these lines to generate a second list of seven lines. It combines these lists into the structure of a sonnet to complete the poem.

###Create a net
Enter a number (sonnets numbered in accordance with Folger Shakespeare's Sonnets and Poems) to create a randomized "net" of a few words (usually between 3 to 7) from that sonnet.
