import Cocoa


// stack -> push,pop

public struct Stack<T>{
    //[]
    fileprivate var array = [T]()
    
    public var count:Int{
        return array.count
    }
    
    public var top:T?{
        return array.last
    }
    
    public var isEmpty:Bool{
        return array.isEmpty
    }
    
    public mutating func push(_ element:T){
        array.append(element)
    }
    
    public mutating func pop() -> T?{
        return array.popLast()
    }
    
}


var stack = Stack<String>()
stack.isEmpty
stack.push("Muchel")
stack.push("Jongeun")
stack.push("Heejin")
stack.isEmpty
stack.count
stack.top // heejin
stack.pop() //heejin
stack.top //jongeun
