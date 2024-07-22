#!/usr/bin/node

const argybargy = process.argv.length;

if (argybargy > 2) {
    console.log('Argument' + (argybargy > 3 ? 's' : '') + ' found');
} else {
    console.log('No argument');
}
