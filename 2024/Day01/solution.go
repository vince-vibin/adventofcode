// https://adventofcode.com/2024/day/1
package main

import (
	"os"
	"fmt"
	"bufio"
	"strings"
	"strconv"
	"sort"
	"errors"
)

func main() {
	input, err := getInput()
	if err != nil {
		fmt.Println(err)
		return
	}

	day1 := day1(parseInput(input))
	fmt.Println(day1)

	day2 := day2(parseInput(input))
	fmt.Println(day2)
}

func day1(leftColumn []int, rightColumn []int) int {
	sort.Ints(leftColumn)
	sort.Ints(rightColumn)
	distance := 0
	for i, num := range leftColumn {
		if rightColumn[i] > num {
			distance = distance + (rightColumn[i] - num)
			continue
		}
		distance = distance + (num - rightColumn[i])
	}
	return distance
}

func day2(leftColumn []int, rightColumn []int) int {
	similarityScore := 0
	for _, num := range leftColumn {
		occurence := 0
		for _, num2 := range rightColumn {
			if num == num2 {
				occurence++
			}
		}
		similarityScore = similarityScore + (num * occurence)
	}
	return similarityScore
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

func parseInput(lines []string) ([]int, []int) {
	var leftColumn []int
	var rightColumn []int
	for _, line := range lines {
		lineSlice := strings.Split(line, "   ")
		left, _ := strconv.Atoi(lineSlice[0])
		right, _ := strconv.Atoi(lineSlice[1])
		leftColumn, rightColumn = append(leftColumn, left), append(rightColumn, right)
	}
	return leftColumn, rightColumn
}
