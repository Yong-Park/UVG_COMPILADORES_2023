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
		CLASS=1, ELSE=2, FI=3, IF=4, IN=5, INHERITS=6, ISVOID=7, LOOP=8, POOL=9, 
		THEN=10, WHILE=11, NEW=12, NOT=13, FALSE=14, TRUE=15, LET=16, INTEGER=17, 
		ID=18, TYPE=19, STRING=20, SEMICOLON=21, OPENBRACE=22, CLOSEBRACE=23, 
		COLON=24, COMMA=25, OPENPARENTHESES=26, CLOSEPARENTHESES=27, DOT=28, AT=29, 
		TILDE=30, MUL=31, ADD=32, SUB=33, DIV=34, EQUAL=35, LT=36, LTEQ=37, ASSIGN=38, 
		OR=39, AND=40, SINGLECOMMENT=41, MULTICOMMENT=42, WS=43, ERROR=44;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"CLASS", "ELSE", "FI", "IF", "IN", "INHERITS", "ISVOID", "LOOP", "POOL", 
			"THEN", "WHILE", "NEW", "NOT", "FALSE", "TRUE", "LET", "INTEGER", "ID", 
			"TYPE", "STRING", "SEMICOLON", "OPENBRACE", "CLOSEBRACE", "COLON", "COMMA", 
			"OPENPARENTHESES", "CLOSEPARENTHESES", "DOT", "AT", "TILDE", "MUL", "ADD", 
			"SUB", "DIV", "EQUAL", "LT", "LTEQ", "ASSIGN", "OR", "AND", "SINGLECOMMENT", 
			"MULTICOMMENT", "WS", "ERROR", "A", "B", "C", "D", "E", "F", "H", "I", 
			"L", "N", "O", "P", "R", "S", "T", "V", "W", "ESC", "UNICODE", "HEX"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, "'false'", "'true'", null, null, null, null, null, "';'", 
			"'{'", "'}'", "':'", "','", "'('", "')'", "'.'", "'@'", "'~'", "'*'", 
			"'+'", "'-'", "'/'", "'='", "'<'", "'<='", "'<-'", "'|'", "'&'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "ELSE", "FI", "IF", "IN", "INHERITS", "ISVOID", "LOOP", 
			"POOL", "THEN", "WHILE", "NEW", "NOT", "FALSE", "TRUE", "LET", "INTEGER", 
			"ID", "TYPE", "STRING", "SEMICOLON", "OPENBRACE", "CLOSEBRACE", "COLON", 
			"COMMA", "OPENPARENTHESES", "CLOSEPARENTHESES", "DOT", "AT", "TILDE", 
			"MUL", "ADD", "SUB", "DIV", "EQUAL", "LT", "LTEQ", "ASSIGN", "OR", "AND", 
			"SINGLECOMMENT", "MULTICOMMENT", "WS", "ERROR"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2.\u0181\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3"+
		"\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3"+
		"\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3"+
		"\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3"+
		"\21\3\21\3\21\3\21\3\22\6\22\u00d5\n\22\r\22\16\22\u00d6\3\23\3\23\7\23"+
		"\u00db\n\23\f\23\16\23\u00de\13\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00ef\n\24\f\24\16\24\u00f2"+
		"\13\24\5\24\u00f4\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00fd\n"+
		"\25\3\25\7\25\u0100\n\25\f\25\16\25\u0103\13\25\3\25\3\25\3\26\3\26\3"+
		"\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3"+
		"\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'"+
		"\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3*\7*\u0135\n*\f*\16*\u0138\13*\3*\3*\3"+
		"+\3+\3+\3+\7+\u0140\n+\f+\16+\u0143\13+\3+\3+\3+\3+\3+\3,\6,\u014b\n,"+
		"\r,\16,\u014c\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3"+
		"\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;"+
		"\3;\3<\3<\3=\3=\3>\3>\3?\3?\3?\5?\u0178\n?\3@\3@\3@\3@\3@\3@\3A\3A\3\u0141"+
		"\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36"+
		";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2"+
		"q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\3\2\35\3\2\62;\3\2c|\6\2\62;C\\aa"+
		"c|\3\2C\\\4\2\13\13^^\4\2\f\f\17\17\6\2\13\f\17\17$$^^\5\2\13\f\16\17"+
		"\"\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2JJjj\4\2KKkk\4"+
		"\2NNnn\4\2PPpp\4\2QQqq\4\2RRrr\4\2TTtt\4\2UUuu\4\2VVvv\4\2XXxx\4\2YYy"+
		"y\n\2$$\61\61^^ddhhppttvv\5\2\62;CHch\2\u017a\2\3\3\2\2\2\2\5\3\2\2\2"+
		"\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3"+
		"\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2"+
		"\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2"+
		"\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2"+
		"\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2"+
		"\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2"+
		"\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y"+
		"\3\2\2\2\3\u0083\3\2\2\2\5\u0089\3\2\2\2\7\u008e\3\2\2\2\t\u0091\3\2\2"+
		"\2\13\u0094\3\2\2\2\r\u0097\3\2\2\2\17\u00a0\3\2\2\2\21\u00a7\3\2\2\2"+
		"\23\u00ac\3\2\2\2\25\u00b1\3\2\2\2\27\u00b6\3\2\2\2\31\u00bc\3\2\2\2\33"+
		"\u00c0\3\2\2\2\35\u00c4\3\2\2\2\37\u00ca\3\2\2\2!\u00cf\3\2\2\2#\u00d4"+
		"\3\2\2\2%\u00d8\3\2\2\2\'\u00f3\3\2\2\2)\u00f5\3\2\2\2+\u0106\3\2\2\2"+
		"-\u0108\3\2\2\2/\u010a\3\2\2\2\61\u010c\3\2\2\2\63\u010e\3\2\2\2\65\u0110"+
		"\3\2\2\2\67\u0112\3\2\2\29\u0114\3\2\2\2;\u0116\3\2\2\2=\u0118\3\2\2\2"+
		"?\u011a\3\2\2\2A\u011c\3\2\2\2C\u011e\3\2\2\2E\u0120\3\2\2\2G\u0122\3"+
		"\2\2\2I\u0124\3\2\2\2K\u0126\3\2\2\2M\u0129\3\2\2\2O\u012c\3\2\2\2Q\u012e"+
		"\3\2\2\2S\u0130\3\2\2\2U\u013b\3\2\2\2W\u014a\3\2\2\2Y\u0150\3\2\2\2["+
		"\u0152\3\2\2\2]\u0154\3\2\2\2_\u0156\3\2\2\2a\u0158\3\2\2\2c\u015a\3\2"+
		"\2\2e\u015c\3\2\2\2g\u015e\3\2\2\2i\u0160\3\2\2\2k\u0162\3\2\2\2m\u0164"+
		"\3\2\2\2o\u0166\3\2\2\2q\u0168\3\2\2\2s\u016a\3\2\2\2u\u016c\3\2\2\2w"+
		"\u016e\3\2\2\2y\u0170\3\2\2\2{\u0172\3\2\2\2}\u0174\3\2\2\2\177\u0179"+
		"\3\2\2\2\u0081\u017f\3\2\2\2\u0083\u0084\5_\60\2\u0084\u0085\5k\66\2\u0085"+
		"\u0086\5[.\2\u0086\u0087\5u;\2\u0087\u0088\5u;\2\u0088\4\3\2\2\2\u0089"+
		"\u008a\5c\62\2\u008a\u008b\5k\66\2\u008b\u008c\5u;\2\u008c\u008d\5c\62"+
		"\2\u008d\6\3\2\2\2\u008e\u008f\5e\63\2\u008f\u0090\5i\65\2\u0090\b\3\2"+
		"\2\2\u0091\u0092\5i\65\2\u0092\u0093\5e\63\2\u0093\n\3\2\2\2\u0094\u0095"+
		"\5i\65\2\u0095\u0096\5m\67\2\u0096\f\3\2\2\2\u0097\u0098\5i\65\2\u0098"+
		"\u0099\5m\67\2\u0099\u009a\5g\64\2\u009a\u009b\5c\62\2\u009b\u009c\5s"+
		":\2\u009c\u009d\5i\65\2\u009d\u009e\5w<\2\u009e\u009f\5u;\2\u009f\16\3"+
		"\2\2\2\u00a0\u00a1\5i\65\2\u00a1\u00a2\5u;\2\u00a2\u00a3\5y=\2\u00a3\u00a4"+
		"\5o8\2\u00a4\u00a5\5i\65\2\u00a5\u00a6\5a\61\2\u00a6\20\3\2\2\2\u00a7"+
		"\u00a8\5k\66\2\u00a8\u00a9\5o8\2\u00a9\u00aa\5o8\2\u00aa\u00ab\5q9\2\u00ab"+
		"\22\3\2\2\2\u00ac\u00ad\5q9\2\u00ad\u00ae\5o8\2\u00ae\u00af\5o8\2\u00af"+
		"\u00b0\5k\66\2\u00b0\24\3\2\2\2\u00b1\u00b2\5w<\2\u00b2\u00b3\5g\64\2"+
		"\u00b3\u00b4\5c\62\2\u00b4\u00b5\5m\67\2\u00b5\26\3\2\2\2\u00b6\u00b7"+
		"\5{>\2\u00b7\u00b8\5g\64\2\u00b8\u00b9\5i\65\2\u00b9\u00ba\5k\66\2\u00ba"+
		"\u00bb\5c\62\2\u00bb\30\3\2\2\2\u00bc\u00bd\5m\67\2\u00bd\u00be\5c\62"+
		"\2\u00be\u00bf\5{>\2\u00bf\32\3\2\2\2\u00c0\u00c1\5m\67\2\u00c1\u00c2"+
		"\5o8\2\u00c2\u00c3\5w<\2\u00c3\34\3\2\2\2\u00c4\u00c5\7h\2\2\u00c5\u00c6"+
		"\7c\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9\7g\2\2\u00c9"+
		"\36\3\2\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7w\2\2\u00cd"+
		"\u00ce\7g\2\2\u00ce \3\2\2\2\u00cf\u00d0\5k\66\2\u00d0\u00d1\5c\62\2\u00d1"+
		"\u00d2\5w<\2\u00d2\"\3\2\2\2\u00d3\u00d5\t\2\2\2\u00d4\u00d3\3\2\2\2\u00d5"+
		"\u00d6\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7$\3\2\2\2"+
		"\u00d8\u00dc\t\3\2\2\u00d9\u00db\t\4\2\2\u00da\u00d9\3\2\2\2\u00db\u00de"+
		"\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd&\3\2\2\2\u00de"+
		"\u00dc\3\2\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7n\2"+
		"\2\u00e2\u00f4\7h\2\2\u00e3\u00e4\7U\2\2\u00e4\u00e5\7G\2\2\u00e5\u00e6"+
		"\7N\2\2\u00e6\u00e7\7H\2\2\u00e7\u00e8\7a\2\2\u00e8\u00e9\7V\2\2\u00e9"+
		"\u00ea\7[\2\2\u00ea\u00eb\7R\2\2\u00eb\u00f4\7G\2\2\u00ec\u00f0\t\5\2"+
		"\2\u00ed\u00ef\t\4\2\2\u00ee\u00ed\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee"+
		"\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3"+
		"\u00df\3\2\2\2\u00f3\u00e3\3\2\2\2\u00f3\u00ec\3\2\2\2\u00f4(\3\2\2\2"+
		"\u00f5\u0101\7$\2\2\u00f6\u00fd\t\6\2\2\u00f7\u00f8\7\17\2\2\u00f8\u00fd"+
		"\7\f\2\2\u00f9\u00fd\t\7\2\2\u00fa\u00fb\7^\2\2\u00fb\u00fd\7$\2\2\u00fc"+
		"\u00f6\3\2\2\2\u00fc\u00f7\3\2\2\2\u00fc\u00f9\3\2\2\2\u00fc\u00fa\3\2"+
		"\2\2\u00fd\u0100\3\2\2\2\u00fe\u0100\n\b\2\2\u00ff\u00fc\3\2\2\2\u00ff"+
		"\u00fe\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2"+
		"\2\2\u0102\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0105\7$\2\2\u0105"+
		"*\3\2\2\2\u0106\u0107\7=\2\2\u0107,\3\2\2\2\u0108\u0109\7}\2\2\u0109."+
		"\3\2\2\2\u010a\u010b\7\177\2\2\u010b\60\3\2\2\2\u010c\u010d\7<\2\2\u010d"+
		"\62\3\2\2\2\u010e\u010f\7.\2\2\u010f\64\3\2\2\2\u0110\u0111\7*\2\2\u0111"+
		"\66\3\2\2\2\u0112\u0113\7+\2\2\u01138\3\2\2\2\u0114\u0115\7\60\2\2\u0115"+
		":\3\2\2\2\u0116\u0117\7B\2\2\u0117<\3\2\2\2\u0118\u0119\7\u0080\2\2\u0119"+
		">\3\2\2\2\u011a\u011b\7,\2\2\u011b@\3\2\2\2\u011c\u011d\7-\2\2\u011dB"+
		"\3\2\2\2\u011e\u011f\7/\2\2\u011fD\3\2\2\2\u0120\u0121\7\61\2\2\u0121"+
		"F\3\2\2\2\u0122\u0123\7?\2\2\u0123H\3\2\2\2\u0124\u0125\7>\2\2\u0125J"+
		"\3\2\2\2\u0126\u0127\7>\2\2\u0127\u0128\7?\2\2\u0128L\3\2\2\2\u0129\u012a"+
		"\7>\2\2\u012a\u012b\7/\2\2\u012bN\3\2\2\2\u012c\u012d\7~\2\2\u012dP\3"+
		"\2\2\2\u012e\u012f\7(\2\2\u012fR\3\2\2\2\u0130\u0131\7/\2\2\u0131\u0132"+
		"\7/\2\2\u0132\u0136\3\2\2\2\u0133\u0135\n\7\2\2\u0134\u0133\3\2\2\2\u0135"+
		"\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139\3\2"+
		"\2\2\u0138\u0136\3\2\2\2\u0139\u013a\b*\2\2\u013aT\3\2\2\2\u013b\u013c"+
		"\7*\2\2\u013c\u013d\7,\2\2\u013d\u0141\3\2\2\2\u013e\u0140\13\2\2\2\u013f"+
		"\u013e\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u0142\3\2\2\2\u0141\u013f\3\2"+
		"\2\2\u0142\u0144\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0145\7,\2\2\u0145"+
		"\u0146\7+\2\2\u0146\u0147\3\2\2\2\u0147\u0148\b+\2\2\u0148V\3\2\2\2\u0149"+
		"\u014b\t\t\2\2\u014a\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014a\3\2"+
		"\2\2\u014c\u014d\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\b,\2\2\u014f"+
		"X\3\2\2\2\u0150\u0151\13\2\2\2\u0151Z\3\2\2\2\u0152\u0153\t\n\2\2\u0153"+
		"\\\3\2\2\2\u0154\u0155\t\13\2\2\u0155^\3\2\2\2\u0156\u0157\t\f\2\2\u0157"+
		"`\3\2\2\2\u0158\u0159\t\r\2\2\u0159b\3\2\2\2\u015a\u015b\t\16\2\2\u015b"+
		"d\3\2\2\2\u015c\u015d\t\17\2\2\u015df\3\2\2\2\u015e\u015f\t\20\2\2\u015f"+
		"h\3\2\2\2\u0160\u0161\t\21\2\2\u0161j\3\2\2\2\u0162\u0163\t\22\2\2\u0163"+
		"l\3\2\2\2\u0164\u0165\t\23\2\2\u0165n\3\2\2\2\u0166\u0167\t\24\2\2\u0167"+
		"p\3\2\2\2\u0168\u0169\t\25\2\2\u0169r\3\2\2\2\u016a\u016b\t\26\2\2\u016b"+
		"t\3\2\2\2\u016c\u016d\t\27\2\2\u016dv\3\2\2\2\u016e\u016f\t\30\2\2\u016f"+
		"x\3\2\2\2\u0170\u0171\t\31\2\2\u0171z\3\2\2\2\u0172\u0173\t\32\2\2\u0173"+
		"|\3\2\2\2\u0174\u0177\7^\2\2\u0175\u0178\t\33\2\2\u0176\u0178\5\177@\2"+
		"\u0177\u0175\3\2\2\2\u0177\u0176\3\2\2\2\u0178~\3\2\2\2\u0179\u017a\7"+
		"w\2\2\u017a\u017b\5\u0081A\2\u017b\u017c\5\u0081A\2\u017c\u017d\5\u0081"+
		"A\2\u017d\u017e\5\u0081A\2\u017e\u0080\3\2\2\2\u017f\u0180\t\34\2\2\u0180"+
		"\u0082\3\2\2\2\16\2\u00d6\u00dc\u00f0\u00f3\u00fc\u00ff\u0101\u0136\u0141"+
		"\u014c\u0177\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}