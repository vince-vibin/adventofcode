package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
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
	var position []int
	turns := map[string]string{
		"up":    "right",
		"right": "down",
		"down":  "left",
		"left":  "up",
	}

	for y, line := range input {
		for x, field := range line {
			if string(field) == "^" {
				position = append(position, x, y)
			}
		}
	}
	direction := "up"
	out := false
	previosPositions := [][]int{}
	for out != true {
		if position[0] < len(input[0])-1 && position[1] < len(input)-1 {
			if direction == "up" {
				if position[1] < len(input[0]) {
					if string(input[position[1]-1][position[0]]) == "#" {
						direction = turns["up"]
						continue
					}
					position[1]--
				} else {
					break
				}
			} else if direction == "right" {
				if position[0] < len(input[0]) {
					if string(input[position[1]][position[0]+1]) == "#" {
						direction = turns["right"]
						continue
					}
					position[0]++
				} else {
					break
				}
			} else if direction == "down" {
				if position[1] < len(input) {
					if string(input[position[1]+1][position[0]]) == "#" {
						direction = turns["down"]
						continue
					}
					position[1]++
				} else {
					break
				}
			} else if direction == "left" {
				if position[0] < len(input[0]) {
					if string(input[position[1]][position[0]-1]) == "#" {
						direction = turns["left"]
						continue
					}
					position[0]--
				} else {
					break
				}
			}
			previosPositions = append(previosPositions, append([]int{}, position...))
		} else {
			out = true
		}
	}
	var distinctPositions [][]int
	seen := make(map[string]bool)
	for _, position := range previosPositions {
		key := fmt.Sprintf("%d,%d", position[0], position[1])
		if !seen[key] {
			seen[key] = true
			distinctPositions = append(distinctPositions, position)
		}
	}
	return len(distinctPositions)
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
