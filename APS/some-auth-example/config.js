const { Scopes } = require('@aps_sdk/authentication');
require('dotenv').config();

let { APS_CLIENT_ID, APS_CLIENT_SECRET, APS_CALLBACK_URL, SERVER_SESSION_SECRET, PORT } = process.env;
if (!APS_CLIENT_ID || !APS_CLIENT_SECRET || !APS_CALLBACK_URL || !SERVER_SESSION_SECRET) {
    console.warn('Missing some of the environment variables.');
    process.exit(1);
}
const INTERNAL_TOKEN_SCOPES = [Scopes.DataRead, Scopes.ViewablesRead,Scopes.DataWrite]; //You can put whatever the scope here
const PUBLIC_TOKEN_SCOPES = [Scopes.ViewablesRead]; // Causes error put otherthan ViewableRead(viewables:read)(the 400 error)
PORT = PORT || 8080;

module.exports = {
    APS_CLIENT_ID,
    APS_CLIENT_SECRET,
    APS_CALLBACK_URL,
    SERVER_SESSION_SECRET,
    INTERNAL_TOKEN_SCOPES,
    PUBLIC_TOKEN_SCOPES,
    PORT
};