#!/usr/bin/node
// check if there are arguments passed to the script

if (process.argv.length === 0) {
    console.log('No argument');
} else if (process.argv.length === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found')
}
