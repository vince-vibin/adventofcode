package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"regexp"
)

func main() {
	input, err := getInput()
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(part1(input))
}

func part1(input []string) int {
	found := 0
	// find horizontal
	for _, line := range input {
		found = found + findMatches(line)
	}
	fmt.Println(found)

	// find vertical
	var verticals []string
	i := 0
	for i < len(input) { // wont work except the input is square because we need to use lenght of the line not number of lines as index
		str := ""
		for _, line := range input {
			str = str + string(line[i])
		}
		verticals = append(verticals, str)
		i++
	}
	for _, line := range verticals {
		found = found + findMatches(line)
	}
	fmt.Println(found)

	// get lenght and height of input
	// for each index on height (exept the last 4 because of xmas word length) go one down and one right
	// do the same for the width
	// to prevent nil pointer you can only go down and right as the current width/height-index
	// add all found numbers to a slice
	// check matches the same way as before

	return found
}

func findMatches(line string) int {
	// need to regexes because of overlapping words
	reXmas := regexp.MustCompile(`(XMAS)`)
	reMasx := regexp.MustCompile(`(MASX)`)
	found := 0
	matches := reXmas.FindAllString(line, -1)
	found = found + len(matches)
	matches = reMasx.FindAllString(line, -1)
	found = found + len(matches)
	return found
}

// --- helpers ---

func getInput() ([]string, error) {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return nil, errors.New("failed to read inputfile")
	}
	defer file.Close()

	var input []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		input = append(input, line)
	}
	return input, nil
}
