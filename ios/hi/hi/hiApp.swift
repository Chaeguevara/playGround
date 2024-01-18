//
//  hiApp.swift
//  hi
//
//  Created by HEEJin Chae on 1/18/24.
//

import SwiftUI

@main
struct hiApp: App {
    var network = Network()
    
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(network)
        }
    }
}
