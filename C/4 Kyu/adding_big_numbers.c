// Helper function to reverse a string in place
#include <stdlib.h>
static void reverse(char *str) {
	int len = strlen(str);
	for (int i = 0; i < len / 2; ++i) {
		char temp = str[i];
		str[i] = str[len - i - 1];
		str[len - i - 1] = temp;
	}
}

// Returns a newly allocated string containing the sum of a and b
char *add(const char *a, const char *b) {
	int len1 = strlen(a);
	int len2 = strlen(b);
	int maxlen = len1 > len2 ? len1 : len2;
	char *result = (char *)malloc(maxlen + 2); // +1 for possible carry, +1 for null
	if (!result) return NULL;

	int carry = 0, i = len1 - 1, j = len2 - 1, k = 0;
	while (i >= 0 || j >= 0 || carry) {
		int digit1 = (i >= 0) ? a[i--] - '0' : 0;
		int digit2 = (j >= 0) ? b[j--] - '0' : 0;
		int sum = digit1 + digit2 + carry;
		result[k++] = (sum % 10) + '0';
		carry = sum / 10;
	}
	result[k] = '\0';
	reverse(result);
	return result;
}