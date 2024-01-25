//
//  ContentView.swift
//  lec3
//
//  Created by HEEJin Chae on 1/25/24.
//

import SwiftUI

struct ContentView: View {
    let emojis: [String] = ["🐻","🍠","🥰","🐯","🐣","🐔","⚽️","🏈","🦁","🐱","🦊"]
    @State var cardCount: Int = 4
    
    var body: some View {
        VStack{
            cards
            cardCountAdjusters
        }
        .padding()
    }
    
    
    func cardCountAdjuster(by offset: Int, symbol: String) -> some View{
        Button(action: {
            cardCount += offset
        },label:{
           Image(systemName: symbol)
        })
        .disabled(cardCount + offset < 1 || cardCount + offset > emojis.count)
    }
   
    var cardCountAdjusters: some View{
        HStack{
            cardRemover
            Spacer()
            cardAdder
        }
        .imageScale(.large)
        .font(.largeTitle)
    }
    var cardRemover: some View{
        cardCountAdjuster(by: -1, symbol: "eraser")
    }
    
    var cardAdder: some View{
        cardCountAdjuster(by: 1, symbol: "plus.diamond")
    }
   
    
    var cards: some View{
        LazyVGrid(columns:[GridItem(.adaptive(minimum: 70))]){
            ForEach(0..<cardCount, id: \.self){ index in
                CardView(content:emojis[index],isFaceUp: true)
                    .aspectRatio(2/3,contentMode: .fit)
            }
        }
        .foregroundColor(.orange)
    }
}


struct CardView: View{
    let content:String
    @State var isFaceUp:Bool = false
    
    var body: some View{
        ZStack{
            let base: RoundedRectangle = RoundedRectangle(cornerRadius: 12)
            Group{
                base.fill(.white)
                base.strokeBorder(lineWidth: 2)
                Text(content).font(.largeTitle)
            }
            base.fill().opacity(isFaceUp ? 0 : 1)
           
        }.onTapGesture {
           print("hi")
            isFaceUp.toggle()
        }
    }
}

#Preview {
    ContentView()
}
