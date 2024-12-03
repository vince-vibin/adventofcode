package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"regexp"
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
	fmt.Println(part2(input))
}

func part1(input []string) int {
	re := regexp.MustCompile(`mul\((\d?\d?\d),(\d?\d?\d)\)`)
	inputStr := ""
	for _, line := range input {
		inputStr = inputStr + line
	}
	result := 0
	matches := re.FindAllString(inputStr, -1)
	for _, match := range matches {
		num1, num2 := strings.Split(match, ",")[0], strings.Split(match, ",")[1]
		num1, num2 = strings.Split(num1, "(")[1], strings.Split(num2, ")")[0]
		num1Int, _ := strconv.Atoi(num1)
		num2Int, _ := strconv.Atoi(num2)
		result = result + (num1Int * num2Int)
	}
	return result
}

func part2(input []string) int {
	inputStr := ""
	for _, line := range input {
		inputStr = inputStr + line
	}
	re := regexp.MustCompile(`mul\(\d+,\d+\)|don't\(\)|do\(\)`)
	matches := re.FindAllString(inputStr, -1)
	enabled := true
	result := 0
	for _, match := range matches {
		if match == "do()" {
			enabled = true
		}
		if match == "don't()" {
			enabled = false
		}
		if strings.HasPrefix(match, "mul(") && enabled {
			num1, num2 := strings.Split(match, ",")[0], strings.Split(match, ",")[1]
			num1, num2 = strings.Split(num1, "(")[1], strings.Split(num2, ")")[0]
			num1Int, _ := strconv.Atoi(num1)
			num2Int, _ := strconv.Atoi(num2)
			result = result + (num1Int * num2Int)
		}
	}
	return result
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
