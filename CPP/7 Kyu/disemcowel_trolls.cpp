# include <string>
std::string disemvowel(std::string str)
{
	std::string vowels = "AEIOUaeiou", result = "";

	for (auto& ch : str)
		if (vowels.find(ch) == std::string::npos)
			result += ch;

	return result;
}