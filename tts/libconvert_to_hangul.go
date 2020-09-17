package main

import (
  "github.com/hangulize/hangulize"
  "C"
)

//export convert_to_hangul
func convert_to_hangul(language *C.char, word *C.char) *C.char {
  return C.CString(hangulize.Hangulize(C.GoString(language), C.GoString(word)))
}

func main() {}

