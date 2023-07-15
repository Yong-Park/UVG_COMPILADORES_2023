// Generated from c:\Users\PARK JONGHYUN\Desktop\Universidad\Cuarto año\Segundo ciclo\compiladores\Lab0_UVG_COMPILADORES_2023\YAPL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, ELSE=2, FALSE=3, TRUE=4, FI=5, IF=6, IN=7, INHERITS=8, ISVOID=9, 
		LOOP=10, POOL=11, THEN=12, WHILE=13, NEW=14, NOT=15, LET=16, NUM=17, ID=18, 
		CLASSTYPE=19, STRING=20, SEMICOLON=21, OPENBRACE=22, CLOSEBRACE=23, COLON=24, 
		COMMA=25, OPENPARENTHESES=26, CLOSEPARENTHESES=27, DOT=28, AT=29, INTEGER_NEGATIVE=30, 
		ADD=31, SUB=32, MUL=33, DIV=34, EQUAL=35, LT=36, LTEQ=37, ASSIGN=38, SINGLECOMMENT=39, 
		MULTICOMMENT=40, WS=41, ERROR=42;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"CLASS", "ELSE", "FALSE", "TRUE", "FI", "IF", "IN", "INHERITS", "ISVOID", 
			"LOOP", "POOL", "THEN", "WHILE", "NEW", "NOT", "LET", "NUM", "ID", "CLASSTYPE", 
			"STRING", "SEMICOLON", "OPENBRACE", "CLOSEBRACE", "COLON", "COMMA", "OPENPARENTHESES", 
			"CLOSEPARENTHESES", "DOT", "AT", "INTEGER_NEGATIVE", "ADD", "SUB", "MUL", 
			"DIV", "EQUAL", "LT", "LTEQ", "ASSIGN", "SINGLECOMMENT", "MULTICOMMENT", 
			"WS", "ERROR", "A", "B", "C", "D", "E", "F", "H", "I", "L", "N", "O", 
			"P", "R", "S", "T", "V", "W", "ESC", "UNICODE", "HEX"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'false'", "'true'", null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, "';'", 
			"'{'", "'}'", "':'", "','", "'('", "')'", "'.'", "'@'", "'~'", "'+'", 
			"'-'", "'*'", "'/'", "'='", "'<'", "'<='", "'<-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "ELSE", "FALSE", "TRUE", "FI", "IF", "IN", "INHERITS", 
			"ISVOID", "LOOP", "POOL", "THEN", "WHILE", "NEW", "NOT", "LET", "NUM", 
			"ID", "CLASSTYPE", "STRING", "SEMICOLON", "OPENBRACE", "CLOSEBRACE", 
			"COLON", "COMMA", "OPENPARENTHESES", "CLOSEPARENTHESES", "DOT", "AT", 
			"INTEGER_NEGATIVE", "ADD", "SUB", "MUL", "DIV", "EQUAL", "LT", "LTEQ", 
			"ASSIGN", "SINGLECOMMENT", "MULTICOMMENT", "WS", "ERROR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public YAPLLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "YAPL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,\u0175\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13"+
		"\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21"+
		"\3\21\3\22\6\22\u00d1\n\22\r\22\16\22\u00d2\3\23\3\23\7\23\u00d7\n\23"+
		"\f\23\16\23\u00da\13\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3"+
		"\24\3\24\7\24\u00e7\n\24\f\24\16\24\u00ea\13\24\5\24\u00ec\n\24\3\25\3"+
		"\25\3\25\3\25\3\25\3\25\3\25\5\25\u00f5\n\25\3\25\7\25\u00f8\n\25\f\25"+
		"\16\25\u00fb\13\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3"+
		"\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3"+
		"!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\7(\u0129"+
		"\n(\f(\16(\u012c\13(\3(\3(\3)\3)\3)\3)\7)\u0134\n)\f)\16)\u0137\13)\3"+
		")\3)\3)\3)\3)\3*\6*\u013f\n*\r*\16*\u0140\3*\3*\3+\3+\3,\3,\3-\3-\3.\3"+
		".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3"+
		"\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3=\5=\u016c\n="+
		"\3>\3>\3>\3>\3>\3>\3?\3?\3\u0135\2@\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n"+
		"\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30"+
		"/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W\2Y\2"+
		"[\2]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\3\2\35\3\2\62;"+
		"\4\2aac|\6\2\62;C\\aac|\3\2C\\\4\2\13\13^^\4\2\f\f\17\17\6\2\13\f\17\17"+
		"$$^^\5\2\13\f\16\17\"\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HH"+
		"hh\4\2JJjj\4\2KKkk\4\2NNnn\4\2PPpp\4\2QQqq\4\2RRrr\4\2TTtt\4\2UUuu\4\2"+
		"VVvv\4\2XXxx\4\2YYyy\n\2$$\61\61^^ddhhppttvv\5\2\62;CHch\2\u016d\2\3\3"+
		"\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2"+
		"\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3"+
		"\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2"+
		"%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61"+
		"\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2"+
		"\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I"+
		"\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2"+
		"\2\2\3\177\3\2\2\2\5\u0085\3\2\2\2\7\u008a\3\2\2\2\t\u0090\3\2\2\2\13"+
		"\u0095\3\2\2\2\r\u0098\3\2\2\2\17\u009b\3\2\2\2\21\u009e\3\2\2\2\23\u00a7"+
		"\3\2\2\2\25\u00ae\3\2\2\2\27\u00b3\3\2\2\2\31\u00b8\3\2\2\2\33\u00bd\3"+
		"\2\2\2\35\u00c3\3\2\2\2\37\u00c7\3\2\2\2!\u00cb\3\2\2\2#\u00d0\3\2\2\2"+
		"%\u00d4\3\2\2\2\'\u00eb\3\2\2\2)\u00ed\3\2\2\2+\u00fe\3\2\2\2-\u0100\3"+
		"\2\2\2/\u0102\3\2\2\2\61\u0104\3\2\2\2\63\u0106\3\2\2\2\65\u0108\3\2\2"+
		"\2\67\u010a\3\2\2\29\u010c\3\2\2\2;\u010e\3\2\2\2=\u0110\3\2\2\2?\u0112"+
		"\3\2\2\2A\u0114\3\2\2\2C\u0116\3\2\2\2E\u0118\3\2\2\2G\u011a\3\2\2\2I"+
		"\u011c\3\2\2\2K\u011e\3\2\2\2M\u0121\3\2\2\2O\u0124\3\2\2\2Q\u012f\3\2"+
		"\2\2S\u013e\3\2\2\2U\u0144\3\2\2\2W\u0146\3\2\2\2Y\u0148\3\2\2\2[\u014a"+
		"\3\2\2\2]\u014c\3\2\2\2_\u014e\3\2\2\2a\u0150\3\2\2\2c\u0152\3\2\2\2e"+
		"\u0154\3\2\2\2g\u0156\3\2\2\2i\u0158\3\2\2\2k\u015a\3\2\2\2m\u015c\3\2"+
		"\2\2o\u015e\3\2\2\2q\u0160\3\2\2\2s\u0162\3\2\2\2u\u0164\3\2\2\2w\u0166"+
		"\3\2\2\2y\u0168\3\2\2\2{\u016d\3\2\2\2}\u0173\3\2\2\2\177\u0080\5[.\2"+
		"\u0080\u0081\5g\64\2\u0081\u0082\5W,\2\u0082\u0083\5q9\2\u0083\u0084\5"+
		"q9\2\u0084\4\3\2\2\2\u0085\u0086\5_\60\2\u0086\u0087\5g\64\2\u0087\u0088"+
		"\5q9\2\u0088\u0089\5_\60\2\u0089\6\3\2\2\2\u008a\u008b\7h\2\2\u008b\u008c"+
		"\7c\2\2\u008c\u008d\7n\2\2\u008d\u008e\7u\2\2\u008e\u008f\7g\2\2\u008f"+
		"\b\3\2\2\2\u0090\u0091\7v\2\2\u0091\u0092\7t\2\2\u0092\u0093\7w\2\2\u0093"+
		"\u0094\7g\2\2\u0094\n\3\2\2\2\u0095\u0096\5a\61\2\u0096\u0097\5e\63\2"+
		"\u0097\f\3\2\2\2\u0098\u0099\5e\63\2\u0099\u009a\5a\61\2\u009a\16\3\2"+
		"\2\2\u009b\u009c\5e\63\2\u009c\u009d\5i\65\2\u009d\20\3\2\2\2\u009e\u009f"+
		"\5e\63\2\u009f\u00a0\5i\65\2\u00a0\u00a1\5c\62\2\u00a1\u00a2\5_\60\2\u00a2"+
		"\u00a3\5o8\2\u00a3\u00a4\5e\63\2\u00a4\u00a5\5s:\2\u00a5\u00a6\5q9\2\u00a6"+
		"\22\3\2\2\2\u00a7\u00a8\5e\63\2\u00a8\u00a9\5q9\2\u00a9\u00aa\5u;\2\u00aa"+
		"\u00ab\5k\66\2\u00ab\u00ac\5e\63\2\u00ac\u00ad\5]/\2\u00ad\24\3\2\2\2"+
		"\u00ae\u00af\5g\64\2\u00af\u00b0\5k\66\2\u00b0\u00b1\5k\66\2\u00b1\u00b2"+
		"\5m\67\2\u00b2\26\3\2\2\2\u00b3\u00b4\5m\67\2\u00b4\u00b5\5k\66\2\u00b5"+
		"\u00b6\5k\66\2\u00b6\u00b7\5g\64\2\u00b7\30\3\2\2\2\u00b8\u00b9\5s:\2"+
		"\u00b9\u00ba\5c\62\2\u00ba\u00bb\5_\60\2\u00bb\u00bc\5i\65\2\u00bc\32"+
		"\3\2\2\2\u00bd\u00be\5w<\2\u00be\u00bf\5c\62\2\u00bf\u00c0\5e\63\2\u00c0"+
		"\u00c1\5g\64\2\u00c1\u00c2\5_\60\2\u00c2\34\3\2\2\2\u00c3\u00c4\5i\65"+
		"\2\u00c4\u00c5\5_\60\2\u00c5\u00c6\5w<\2\u00c6\36\3\2\2\2\u00c7\u00c8"+
		"\5i\65\2\u00c8\u00c9\5k\66\2\u00c9\u00ca\5s:\2\u00ca \3\2\2\2\u00cb\u00cc"+
		"\5g\64\2\u00cc\u00cd\5_\60\2\u00cd\u00ce\5s:\2\u00ce\"\3\2\2\2\u00cf\u00d1"+
		"\t\2\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2"+
		"\u00d3\3\2\2\2\u00d3$\3\2\2\2\u00d4\u00d8\t\3\2\2\u00d5\u00d7\t\4\2\2"+
		"\u00d6\u00d5\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9"+
		"\3\2\2\2\u00d9&\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dc\7U\2\2\u00dc\u00dd"+
		"\7G\2\2\u00dd\u00de\7N\2\2\u00de\u00df\7H\2\2\u00df\u00e0\7a\2\2\u00e0"+
		"\u00e1\7V\2\2\u00e1\u00e2\7[\2\2\u00e2\u00e3\7R\2\2\u00e3\u00ec\7G\2\2"+
		"\u00e4\u00e8\t\5\2\2\u00e5\u00e7\t\4\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00ea"+
		"\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea"+
		"\u00e8\3\2\2\2\u00eb\u00db\3\2\2\2\u00eb\u00e4\3\2\2\2\u00ec(\3\2\2\2"+
		"\u00ed\u00f9\7$\2\2\u00ee\u00f5\t\6\2\2\u00ef\u00f0\7\17\2\2\u00f0\u00f5"+
		"\7\f\2\2\u00f1\u00f5\t\7\2\2\u00f2\u00f3\7^\2\2\u00f3\u00f5\7$\2\2\u00f4"+
		"\u00ee\3\2\2\2\u00f4\u00ef\3\2\2\2\u00f4\u00f1\3\2\2\2\u00f4\u00f2\3\2"+
		"\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f8\n\b\2\2\u00f7\u00f4\3\2\2\2\u00f7"+
		"\u00f6\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2"+
		"\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\7$\2\2\u00fd"+
		"*\3\2\2\2\u00fe\u00ff\7=\2\2\u00ff,\3\2\2\2\u0100\u0101\7}\2\2\u0101."+
		"\3\2\2\2\u0102\u0103\7\177\2\2\u0103\60\3\2\2\2\u0104\u0105\7<\2\2\u0105"+
		"\62\3\2\2\2\u0106\u0107\7.\2\2\u0107\64\3\2\2\2\u0108\u0109\7*\2\2\u0109"+
		"\66\3\2\2\2\u010a\u010b\7+\2\2\u010b8\3\2\2\2\u010c\u010d\7\60\2\2\u010d"+
		":\3\2\2\2\u010e\u010f\7B\2\2\u010f<\3\2\2\2\u0110\u0111\7\u0080\2\2\u0111"+
		">\3\2\2\2\u0112\u0113\7-\2\2\u0113@\3\2\2\2\u0114\u0115\7/\2\2\u0115B"+
		"\3\2\2\2\u0116\u0117\7,\2\2\u0117D\3\2\2\2\u0118\u0119\7\61\2\2\u0119"+
		"F\3\2\2\2\u011a\u011b\7?\2\2\u011bH\3\2\2\2\u011c\u011d\7>\2\2\u011dJ"+
		"\3\2\2\2\u011e\u011f\7>\2\2\u011f\u0120\7?\2\2\u0120L\3\2\2\2\u0121\u0122"+
		"\7>\2\2\u0122\u0123\7/\2\2\u0123N\3\2\2\2\u0124\u0125\7/\2\2\u0125\u0126"+
		"\7/\2\2\u0126\u012a\3\2\2\2\u0127\u0129\n\7\2\2\u0128\u0127\3\2\2\2\u0129"+
		"\u012c\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012d\3\2"+
		"\2\2\u012c\u012a\3\2\2\2\u012d\u012e\b(\2\2\u012eP\3\2\2\2\u012f\u0130"+
		"\7*\2\2\u0130\u0131\7,\2\2\u0131\u0135\3\2\2\2\u0132\u0134\13\2\2\2\u0133"+
		"\u0132\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0136\3\2\2\2\u0135\u0133\3\2"+
		"\2\2\u0136\u0138\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0139\7,\2\2\u0139"+
		"\u013a\7+\2\2\u013a\u013b\3\2\2\2\u013b\u013c\b)\2\2\u013cR\3\2\2\2\u013d"+
		"\u013f\t\t\2\2\u013e\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u013e\3\2"+
		"\2\2\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\b*\2\2\u0143"+
		"T\3\2\2\2\u0144\u0145\13\2\2\2\u0145V\3\2\2\2\u0146\u0147\t\n\2\2\u0147"+
		"X\3\2\2\2\u0148\u0149\t\13\2\2\u0149Z\3\2\2\2\u014a\u014b\t\f\2\2\u014b"+
		"\\\3\2\2\2\u014c\u014d\t\r\2\2\u014d^\3\2\2\2\u014e\u014f\t\16\2\2\u014f"+
		"`\3\2\2\2\u0150\u0151\t\17\2\2\u0151b\3\2\2\2\u0152\u0153\t\20\2\2\u0153"+
		"d\3\2\2\2\u0154\u0155\t\21\2\2\u0155f\3\2\2\2\u0156\u0157\t\22\2\2\u0157"+
		"h\3\2\2\2\u0158\u0159\t\23\2\2\u0159j\3\2\2\2\u015a\u015b\t\24\2\2\u015b"+
		"l\3\2\2\2\u015c\u015d\t\25\2\2\u015dn\3\2\2\2\u015e\u015f\t\26\2\2\u015f"+
		"p\3\2\2\2\u0160\u0161\t\27\2\2\u0161r\3\2\2\2\u0162\u0163\t\30\2\2\u0163"+
		"t\3\2\2\2\u0164\u0165\t\31\2\2\u0165v\3\2\2\2\u0166\u0167\t\32\2\2\u0167"+
		"x\3\2\2\2\u0168\u016b\7^\2\2\u0169\u016c\t\33\2\2\u016a\u016c\5{>\2\u016b"+
		"\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016cz\3\2\2\2\u016d\u016e\7w\2\2\u016e"+
		"\u016f\5}?\2\u016f\u0170\5}?\2\u0170\u0171\5}?\2\u0171\u0172\5}?\2\u0172"+
		"|\3\2\2\2\u0173\u0174\t\34\2\2\u0174~\3\2\2\2\16\2\u00d2\u00d8\u00e8\u00eb"+
		"\u00f4\u00f7\u00f9\u012a\u0135\u0140\u016b\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}