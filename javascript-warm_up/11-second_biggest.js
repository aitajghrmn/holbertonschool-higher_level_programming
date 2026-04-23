#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  // Diziyi büyükten küçüğe sırala
  args.sort((a, b) => b - a);
  // Birinci en büyük (args[0]) hariç, ikinci en büyüğü yazdır
  console.log(args[1]);
}
