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
	var rules [][]int
	newline := 0
	for i, line := range input {
		if line == "" {
			newline = i
			break
		}
		var rule []int
		for _, str := range strings.Split(line, "|") {
			num, _ := strconv.Atoi(str)
			rule = append(rule, num)
		}
		rules = append(rules, rule)
	}

	var updates [][]int
	for _, line := range input[newline+1:] {
		var update []int
		for _, str := range strings.Split(line, ",") {
			num, _ := strconv.Atoi(str)
			update = append(update, num)
		}
		updates = append(updates, update)
	}

	var validUpdates [][]int
	for _, update := range updates {
		updateValid := true
		for index, page := range update {
			var matchingRules [][]int
			for _, rule := range rules {
				for _, num := range rule {
					if num == page {
						matchingRules = append(matchingRules, rule)
						continue
					}
				}
			}
			for _, rule := range matchingRules {
				var position int
				for i, num := range rule {
					if num == page {
						position = i
					}
				}
				if position == 0 { // shouldnt occure before so we check before
					for _, num := range update[:index] {
						if num == rule[1] {
							updateValid = false
							break
						}
					}
					continue
				}
				if position == 1 { // shouldnt occure after so we check after
					for _, num := range update[index:] {
						if num == rule[0] {
							updateValid = false
							break
						}
					}
					continue
				}
			}
		}
		if updateValid {
			validUpdates = append(validUpdates, update)
		}
	}

	sum := 0
	for _, update := range validUpdates {
		sum = sum + update[len(update)/2]
	}

	return sum
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
