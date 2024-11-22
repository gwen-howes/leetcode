public class Solution {
    public bool IsValid(string s) {
        Dictionary<char, char> brackets = new Dictionary<char, char>{ 
            {')', '('}, 
            {'}', '{'}, 
            {']', '['} 
        };
        Stack<char> stack = new Stack<char>();
        
        foreach(char bracket in s) {
            if (brackets.ContainsKey(bracket)) {
                if (stack.Count > 0 && brackets[bracket] == stack.Peek()) {
                    stack.Pop();
                } else {
                    return false;
                }
            } else {
                stack.Push(bracket);
            }
        }
        return stack.Count == 0;
    }
}