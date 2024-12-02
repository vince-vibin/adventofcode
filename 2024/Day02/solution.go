package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
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
	safe := 0
	for _, line := range input {
		lineSlice := strings.Split(line, " ")
		var lineInt []int
		for _, num := range lineSlice {
			parsed, _ := strconv.Atoi(num)
			lineInt = append(lineInt, parsed)
		}

		isValid := true
		if lineInt[0] < lineInt[1] { // increasing
			for i := 0; i < len(lineInt)-1; i++ {
				diff := lineInt[i+1] - lineInt[i]
				if diff > 3 || diff < 1 {
					isValid = false
					break
				}
			}
		} else if lineInt[0] > lineInt[1] { // decreasing
			for i := 0; i < len(lineInt)-1; i++ {
				diff := lineInt[i] - lineInt[i+1]
				if diff > 3 || diff < 1 {
					isValid = false
					break
				}
			}
		} else {
			continue
		}
		if isValid {
			safe = safe + 1
		}
	}
	return safe
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
