

package util

import (
	"errors"
	"fmt"
	"strings"
)

func Trim(s string) (string, error) {
	if s == "" {
		return "", errors.New("input string is empty")
	}
	return strings.TrimSpace(s), nil
}

func ToLower(s string) (string, error) {
	if s == "" {
		return "", errors.New("input string is empty")
	}
	return strings.ToLower(s), nil
}

func ToUpper(s string) (string, error) {
	if s == "" {
		return "", errors.New("input string is empty")
	}
	return strings.ToUpper(s), nil
}

func Contains(s, substr string) (bool, error) {
	if s == "" || substr == "" {
		return false, errors.New("input strings are empty")
	}
	return strings.Contains(s, substr), nil
}

func StartsWith(s, prefix string) (bool, error) {
	if s == "" || prefix == "" {
		return false, errors.New("input strings are empty")
	}
	return strings.HasPrefix(s, prefix), nil
}

func EndsWith(s, suffix string) (bool, error) {
	if s == "" || suffix == "" {
		return false, errors.New("input strings are empty")
	}
	return strings.HasSuffix(s, suffix), nil
}

func Index(s, substr string) (int, error) {
	if s == "" || substr == "" {
		return -1, errors.New("input strings are empty")
	}
	return strings.Index(s, substr), nil
}

func LastIndex(s, substr string) (int, error) {
	if s == "" || substr == "" {
		return -1, errors.New("input strings are empty")
	}
	return strings.LastIndex(s, substr), nil
}

func Replace(s, old, new string) (string, error) {
	if s == "" || old == "" || new == "" {
		return "", errors.New("input strings are empty")
	}
	return strings.Replace(s, old, new, -1), nil
}

func Split(s, sep string) ([]string, error) {
	if s == "" || sep == "" {
		return nil, errors.New("input strings are empty")
	}
	return strings.Split(s, sep), nil
}

func Join(a []string, sep string) (string, error) {
	if len(a) == 0 || sep == "" {
		return "", errors.New("input slice is empty or separator is empty")
	}
	return strings.Join(a, sep), nil
}

func Format(format string, a ...interface{}) (string, error) {
	if format == "" {
		return "", errors.New("format string is empty")
	}
	return fmt.Sprintf(format, a...), nil
}