// Generated from c:/Users/PARK JONGHYUN/Desktop/Universidad/Cuarto año/Segundo ciclo/compiladores/Lab0_UVG_COMPILADORES_2023/YAPL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class YAPLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

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
	public static final int
		RULE_program = 0, RULE_classDefine = 1, RULE_feature = 2, RULE_formal = 3, 
		RULE_expr = 4, RULE_let_expr = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "classDefine", "feature", "formal", "expr", "let_expr"
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

	@Override
	public String getGrammarFileName() { return "YAPL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YAPLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	 
		public ProgramContext() { }
		public void copyFrom(ProgramContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StartContext extends ProgramContext {
		public List<ClassDefineContext> classDefine() {
			return getRuleContexts(ClassDefineContext.class);
		}
		public ClassDefineContext classDefine(int i) {
			return getRuleContext(ClassDefineContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(YAPLParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YAPLParser.SEMICOLON, i);
		}
		public StartContext(ProgramContext ctx) { copyFrom(ctx); }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			_localctx = new StartContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(15); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(12);
				classDefine();
				setState(13);
				match(SEMICOLON);
				}
				}
				setState(17); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CLASS );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassDefineContext extends ParserRuleContext {
		public ClassDefineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDefine; }
	 
		public ClassDefineContext() { }
		public void copyFrom(ClassDefineContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DefClaseContext extends ClassDefineContext {
		public TerminalNode CLASS() { return getToken(YAPLParser.CLASS, 0); }
		public List<TerminalNode> TYPE() { return getTokens(YAPLParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(YAPLParser.TYPE, i);
		}
		public TerminalNode OPENBRACE() { return getToken(YAPLParser.OPENBRACE, 0); }
		public TerminalNode CLOSEBRACE() { return getToken(YAPLParser.CLOSEBRACE, 0); }
		public TerminalNode INHERITS() { return getToken(YAPLParser.INHERITS, 0); }
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(YAPLParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YAPLParser.SEMICOLON, i);
		}
		public DefClaseContext(ClassDefineContext ctx) { copyFrom(ctx); }
	}

	public final ClassDefineContext classDefine() throws RecognitionException {
		ClassDefineContext _localctx = new ClassDefineContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_classDefine);
		int _la;
		try {
			_localctx = new DefClaseContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			match(CLASS);
			setState(20);
			match(TYPE);
			setState(23);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITS) {
				{
				setState(21);
				match(INHERITS);
				setState(22);
				match(TYPE);
				}
			}

			setState(25);
			match(OPENBRACE);
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(26);
				feature();
				setState(27);
				match(SEMICOLON);
				}
				}
				setState(33);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(34);
			match(CLOSEBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FeatureContext extends ParserRuleContext {
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	 
		public FeatureContext() { }
		public void copyFrom(FeatureContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MethodContext extends FeatureContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode OPENPARENTHESES() { return getToken(YAPLParser.OPENPARENTHESES, 0); }
		public TerminalNode CLOSEPARENTHESES() { return getToken(YAPLParser.CLOSEPARENTHESES, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public TerminalNode OPENBRACE() { return getToken(YAPLParser.OPENBRACE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSEBRACE() { return getToken(YAPLParser.CLOSEBRACE, 0); }
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(YAPLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YAPLParser.COMMA, i);
		}
		public MethodContext(FeatureContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PropertyContext extends FeatureContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public PropertyContext(FeatureContext ctx) { copyFrom(ctx); }
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_feature);
		int _la;
		try {
			setState(62);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				_localctx = new MethodContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(36);
				match(ID);
				setState(37);
				match(OPENPARENTHESES);
				setState(46);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(38);
					formal();
					setState(43);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(39);
						match(COMMA);
						setState(40);
						formal();
						}
						}
						setState(45);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(48);
				match(CLOSEPARENTHESES);
				setState(49);
				match(COLON);
				setState(50);
				match(TYPE);
				setState(51);
				match(OPENBRACE);
				setState(52);
				expr(0);
				setState(53);
				match(CLOSEBRACE);
				}
				break;
			case 2:
				_localctx = new PropertyContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				match(ID);
				setState(56);
				match(COLON);
				setState(57);
				match(TYPE);
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(58);
					match(ASSIGN);
					setState(59);
					expr(0);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FormalContext extends ParserRuleContext {
		public FormalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal; }
	 
		public FormalContext() { }
		public void copyFrom(FormalContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FormlContext extends FormalContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public FormlContext(FormalContext ctx) { copyFrom(ctx); }
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_formal);
		try {
			_localctx = new FormlContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(ID);
			setState(65);
			match(COLON);
			setState(66);
			match(TYPE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SubContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode SUB() { return getToken(YAPLParser.SUB, 0); }
		public SubContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringContext extends ExprContext {
		public TerminalNode STRING() { return getToken(YAPLParser.STRING, 0); }
		public StringContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(YAPLParser.MUL, 0); }
		public MulContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LteqContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LTEQ() { return getToken(YAPLParser.LTEQ, 0); }
		public LteqContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LtContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LT() { return getToken(YAPLParser.LT, 0); }
		public LtContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WhileContext extends ExprContext {
		public TerminalNode WHILE() { return getToken(YAPLParser.WHILE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LOOP() { return getToken(YAPLParser.LOOP, 0); }
		public TerminalNode POOL() { return getToken(YAPLParser.POOL, 0); }
		public WhileContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DivContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode DIV() { return getToken(YAPLParser.DIV, 0); }
		public DivContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NotContext extends ExprContext {
		public TerminalNode NOT() { return getToken(YAPLParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NotContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NewObjectContext extends ExprContext {
		public TerminalNode NEW() { return getToken(YAPLParser.NEW, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public NewObjectContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AndContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode AND() { return getToken(YAPLParser.AND, 0); }
		public AndContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ExprContext {
		public TerminalNode OPENBRACE() { return getToken(YAPLParser.OPENBRACE, 0); }
		public TerminalNode CLOSEBRACE() { return getToken(YAPLParser.CLOSEBRACE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(YAPLParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YAPLParser.SEMICOLON, i);
		}
		public BlockContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LetContext extends ExprContext {
		public TerminalNode LET() { return getToken(YAPLParser.LET, 0); }
		public Let_exprContext let_expr() {
			return getRuleContext(Let_exprContext.class,0);
		}
		public LetContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdContext extends ExprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public IdContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfContext extends ExprContext {
		public TerminalNode IF() { return getToken(YAPLParser.IF, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode THEN() { return getToken(YAPLParser.THEN, 0); }
		public TerminalNode ELSE() { return getToken(YAPLParser.ELSE, 0); }
		public TerminalNode FI() { return getToken(YAPLParser.FI, 0); }
		public IfContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OwnMethodCallContext extends ExprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode OPENPARENTHESES() { return getToken(YAPLParser.OPENPARENTHESES, 0); }
		public TerminalNode CLOSEPARENTHESES() { return getToken(YAPLParser.CLOSEPARENTHESES, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(YAPLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YAPLParser.COMMA, i);
		}
		public OwnMethodCallContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class INTEGERContext extends ExprContext {
		public TerminalNode INTEGER() { return getToken(YAPLParser.INTEGER, 0); }
		public INTEGERContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ADD() { return getToken(YAPLParser.ADD, 0); }
		public AddContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VoidContext extends ExprContext {
		public TerminalNode ISVOID() { return getToken(YAPLParser.ISVOID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public VoidContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OrContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode OR() { return getToken(YAPLParser.OR, 0); }
		public OrContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class InvertContext extends ExprContext {
		public TerminalNode TILDE() { return getToken(YAPLParser.TILDE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public InvertContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FactExprContext extends ExprContext {
		public TerminalNode OPENPARENTHESES() { return getToken(YAPLParser.OPENPARENTHESES, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSEPARENTHESES() { return getToken(YAPLParser.CLOSEPARENTHESES, 0); }
		public FactExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FalseContext extends ExprContext {
		public TerminalNode FALSE() { return getToken(YAPLParser.FALSE, 0); }
		public FalseContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class EqualContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode EQUAL() { return getToken(YAPLParser.EQUAL, 0); }
		public EqualContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TrueContext extends ExprContext {
		public TerminalNode TRUE() { return getToken(YAPLParser.TRUE, 0); }
		public TrueContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ExprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MethodCallContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode DOT() { return getToken(YAPLParser.DOT, 0); }
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode OPENPARENTHESES() { return getToken(YAPLParser.OPENPARENTHESES, 0); }
		public TerminalNode CLOSEPARENTHESES() { return getToken(YAPLParser.CLOSEPARENTHESES, 0); }
		public TerminalNode AT() { return getToken(YAPLParser.AT, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public List<TerminalNode> COMMA() { return getTokens(YAPLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YAPLParser.COMMA, i);
		}
		public MethodCallContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				_localctx = new OwnMethodCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(69);
				match(ID);
				setState(70);
				match(OPENPARENTHESES);
				setState(79);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1146615952L) != 0)) {
					{
					setState(71);
					expr(0);
					setState(76);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(72);
						match(COMMA);
						setState(73);
						expr(0);
						}
						}
						setState(78);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(81);
				match(CLOSEPARENTHESES);
				}
				break;
			case 2:
				{
				_localctx = new IfContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(82);
				match(IF);
				setState(83);
				expr(0);
				setState(84);
				match(THEN);
				setState(85);
				expr(0);
				setState(86);
				match(ELSE);
				setState(87);
				expr(0);
				setState(88);
				match(FI);
				}
				break;
			case 3:
				{
				_localctx = new WhileContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(90);
				match(WHILE);
				setState(91);
				expr(0);
				setState(92);
				match(LOOP);
				setState(93);
				expr(0);
				setState(94);
				match(POOL);
				}
				break;
			case 4:
				{
				_localctx = new BlockContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(96);
				match(OPENBRACE);
				setState(100); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(97);
					expr(0);
					setState(98);
					match(SEMICOLON);
					}
					}
					setState(102); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1146615952L) != 0) );
				setState(104);
				match(CLOSEBRACE);
				}
				break;
			case 5:
				{
				_localctx = new LetContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(106);
				match(LET);
				setState(107);
				let_expr();
				}
				break;
			case 6:
				{
				_localctx = new NewObjectContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(108);
				match(NEW);
				setState(109);
				match(TYPE);
				}
				break;
			case 7:
				{
				_localctx = new InvertContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(110);
				match(TILDE);
				setState(111);
				expr(19);
				}
				break;
			case 8:
				{
				_localctx = new VoidContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(112);
				match(ISVOID);
				setState(113);
				expr(18);
				}
				break;
			case 9:
				{
				_localctx = new NotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(114);
				match(NOT);
				setState(115);
				expr(8);
				}
				break;
			case 10:
				{
				_localctx = new FactExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(116);
				match(OPENPARENTHESES);
				setState(117);
				expr(0);
				setState(118);
				match(CLOSEPARENTHESES);
				}
				break;
			case 11:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(120);
				match(ID);
				}
				break;
			case 12:
				{
				_localctx = new INTEGERContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(121);
				match(INTEGER);
				}
				break;
			case 13:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(122);
				match(STRING);
				}
				break;
			case 14:
				{
				_localctx = new TrueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(123);
				match(TRUE);
				}
				break;
			case 15:
				{
				_localctx = new FalseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(124);
				match(FALSE);
				}
				break;
			case 16:
				{
				_localctx = new AssignContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(125);
				match(ID);
				setState(126);
				match(ASSIGN);
				setState(127);
				expr(1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(178);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(176);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
					case 1:
						{
						_localctx = new MulContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(130);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(131);
						match(MUL);
						setState(132);
						expr(18);
						}
						break;
					case 2:
						{
						_localctx = new DivContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(133);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(134);
						match(DIV);
						setState(135);
						expr(17);
						}
						break;
					case 3:
						{
						_localctx = new AddContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(136);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(137);
						match(ADD);
						setState(138);
						expr(16);
						}
						break;
					case 4:
						{
						_localctx = new SubContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(139);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(140);
						match(SUB);
						setState(141);
						expr(15);
						}
						break;
					case 5:
						{
						_localctx = new LteqContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(142);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(143);
						match(LTEQ);
						setState(144);
						expr(14);
						}
						break;
					case 6:
						{
						_localctx = new LtContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(145);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(146);
						match(LT);
						setState(147);
						expr(13);
						}
						break;
					case 7:
						{
						_localctx = new EqualContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(148);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(149);
						match(EQUAL);
						setState(150);
						expr(12);
						}
						break;
					case 8:
						{
						_localctx = new OrContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(151);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(152);
						match(OR);
						setState(153);
						expr(11);
						}
						break;
					case 9:
						{
						_localctx = new AndContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(154);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(155);
						match(AND);
						setState(156);
						expr(10);
						}
						break;
					case 10:
						{
						_localctx = new MethodCallContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(157);
						if (!(precpred(_ctx, 26))) throw new FailedPredicateException(this, "precpred(_ctx, 26)");
						setState(160);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==AT) {
							{
							setState(158);
							match(AT);
							setState(159);
							match(TYPE);
							}
						}

						setState(162);
						match(DOT);
						setState(163);
						match(ID);
						setState(164);
						match(OPENPARENTHESES);
						setState(173);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1146615952L) != 0)) {
							{
							setState(165);
							expr(0);
							setState(170);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==COMMA) {
								{
								{
								setState(166);
								match(COMMA);
								setState(167);
								expr(0);
								}
								}
								setState(172);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(175);
						match(CLOSEPARENTHESES);
						}
						break;
					}
					} 
				}
				setState(180);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Let_exprContext extends ParserRuleContext {
		public Let_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_let_expr; }
	 
		public Let_exprContext() { }
		public void copyFrom(Let_exprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LetInContext extends Let_exprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public TerminalNode IN() { return getToken(YAPLParser.IN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public LetInContext(Let_exprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LetAssignLetContext extends Let_exprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(YAPLParser.COMMA, 0); }
		public Let_exprContext let_expr() {
			return getRuleContext(Let_exprContext.class,0);
		}
		public LetAssignLetContext(Let_exprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LetAssignInContext extends Let_exprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode IN() { return getToken(YAPLParser.IN, 0); }
		public LetAssignInContext(Let_exprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NestedLetContext extends Let_exprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public TerminalNode COMMA() { return getToken(YAPLParser.COMMA, 0); }
		public Let_exprContext let_expr() {
			return getRuleContext(Let_exprContext.class,0);
		}
		public NestedLetContext(Let_exprContext ctx) { copyFrom(ctx); }
	}

	public final Let_exprContext let_expr() throws RecognitionException {
		Let_exprContext _localctx = new Let_exprContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_let_expr);
		try {
			setState(207);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				_localctx = new NestedLetContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(181);
				match(ID);
				setState(182);
				match(COLON);
				setState(183);
				match(TYPE);
				setState(184);
				match(COMMA);
				setState(185);
				let_expr();
				}
				break;
			case 2:
				_localctx = new LetInContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(186);
				match(ID);
				setState(187);
				match(COLON);
				setState(188);
				match(TYPE);
				setState(189);
				match(IN);
				setState(190);
				expr(0);
				}
				break;
			case 3:
				_localctx = new LetAssignLetContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(191);
				match(ID);
				setState(192);
				match(COLON);
				setState(193);
				match(TYPE);
				setState(194);
				match(ASSIGN);
				setState(195);
				expr(0);
				setState(196);
				match(COMMA);
				setState(197);
				let_expr();
				}
				break;
			case 4:
				_localctx = new LetAssignInContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(199);
				match(ID);
				setState(200);
				match(COLON);
				setState(201);
				match(TYPE);
				setState(202);
				match(ASSIGN);
				setState(203);
				expr(0);
				setState(204);
				match(IN);
				setState(205);
				expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 17);
		case 1:
			return precpred(_ctx, 16);
		case 2:
			return precpred(_ctx, 15);
		case 3:
			return precpred(_ctx, 14);
		case 4:
			return precpred(_ctx, 13);
		case 5:
			return precpred(_ctx, 12);
		case 6:
			return precpred(_ctx, 11);
		case 7:
			return precpred(_ctx, 10);
		case 8:
			return precpred(_ctx, 9);
		case 9:
			return precpred(_ctx, 26);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001,\u00d2\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0001\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u0010"+
		"\b\u0000\u000b\u0000\f\u0000\u0011\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001\u0018\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0005\u0001\u001e\b\u0001\n\u0001\f\u0001!\t\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0005\u0002*\b\u0002\n\u0002\f\u0002-\t\u0002\u0003\u0002/\b\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002=\b\u0002\u0003\u0002?\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0005\u0004K\b\u0004\n\u0004\f\u0004N\t\u0004\u0003"+
		"\u0004P\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0004\u0004e\b\u0004\u000b\u0004\f\u0004"+
		"f\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u0004\u0081\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u0004\u00a1\b\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004\u00a9\b\u0004"+
		"\n\u0004\f\u0004\u00ac\t\u0004\u0003\u0004\u00ae\b\u0004\u0001\u0004\u0005"+
		"\u0004\u00b1\b\u0004\n\u0004\f\u0004\u00b4\t\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005\u00d0\b\u0005\u0001\u0005\u0000\u0001\b\u0006\u0000\u0002"+
		"\u0004\u0006\b\n\u0000\u0000\u00f4\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0002\u0013\u0001\u0000\u0000\u0000\u0004>\u0001\u0000\u0000\u0000\u0006"+
		"@\u0001\u0000\u0000\u0000\b\u0080\u0001\u0000\u0000\u0000\n\u00cf\u0001"+
		"\u0000\u0000\u0000\f\r\u0003\u0002\u0001\u0000\r\u000e\u0005\u0015\u0000"+
		"\u0000\u000e\u0010\u0001\u0000\u0000\u0000\u000f\f\u0001\u0000\u0000\u0000"+
		"\u0010\u0011\u0001\u0000\u0000\u0000\u0011\u000f\u0001\u0000\u0000\u0000"+
		"\u0011\u0012\u0001\u0000\u0000\u0000\u0012\u0001\u0001\u0000\u0000\u0000"+
		"\u0013\u0014\u0005\u0001\u0000\u0000\u0014\u0017\u0005\u0013\u0000\u0000"+
		"\u0015\u0016\u0005\u0006\u0000\u0000\u0016\u0018\u0005\u0013\u0000\u0000"+
		"\u0017\u0015\u0001\u0000\u0000\u0000\u0017\u0018\u0001\u0000\u0000\u0000"+
		"\u0018\u0019\u0001\u0000\u0000\u0000\u0019\u001f\u0005\u0016\u0000\u0000"+
		"\u001a\u001b\u0003\u0004\u0002\u0000\u001b\u001c\u0005\u0015\u0000\u0000"+
		"\u001c\u001e\u0001\u0000\u0000\u0000\u001d\u001a\u0001\u0000\u0000\u0000"+
		"\u001e!\u0001\u0000\u0000\u0000\u001f\u001d\u0001\u0000\u0000\u0000\u001f"+
		" \u0001\u0000\u0000\u0000 \"\u0001\u0000\u0000\u0000!\u001f\u0001\u0000"+
		"\u0000\u0000\"#\u0005\u0017\u0000\u0000#\u0003\u0001\u0000\u0000\u0000"+
		"$%\u0005\u0012\u0000\u0000%.\u0005\u001a\u0000\u0000&+\u0003\u0006\u0003"+
		"\u0000\'(\u0005\u0019\u0000\u0000(*\u0003\u0006\u0003\u0000)\'\u0001\u0000"+
		"\u0000\u0000*-\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000+,\u0001"+
		"\u0000\u0000\u0000,/\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000"+
		".&\u0001\u0000\u0000\u0000./\u0001\u0000\u0000\u0000/0\u0001\u0000\u0000"+
		"\u000001\u0005\u001b\u0000\u000012\u0005\u0018\u0000\u000023\u0005\u0013"+
		"\u0000\u000034\u0005\u0016\u0000\u000045\u0003\b\u0004\u000056\u0005\u0017"+
		"\u0000\u00006?\u0001\u0000\u0000\u000078\u0005\u0012\u0000\u000089\u0005"+
		"\u0018\u0000\u00009<\u0005\u0013\u0000\u0000:;\u0005&\u0000\u0000;=\u0003"+
		"\b\u0004\u0000<:\u0001\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=?\u0001"+
		"\u0000\u0000\u0000>$\u0001\u0000\u0000\u0000>7\u0001\u0000\u0000\u0000"+
		"?\u0005\u0001\u0000\u0000\u0000@A\u0005\u0012\u0000\u0000AB\u0005\u0018"+
		"\u0000\u0000BC\u0005\u0013\u0000\u0000C\u0007\u0001\u0000\u0000\u0000"+
		"DE\u0006\u0004\uffff\uffff\u0000EF\u0005\u0012\u0000\u0000FO\u0005\u001a"+
		"\u0000\u0000GL\u0003\b\u0004\u0000HI\u0005\u0019\u0000\u0000IK\u0003\b"+
		"\u0004\u0000JH\u0001\u0000\u0000\u0000KN\u0001\u0000\u0000\u0000LJ\u0001"+
		"\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MP\u0001\u0000\u0000\u0000"+
		"NL\u0001\u0000\u0000\u0000OG\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000"+
		"\u0000PQ\u0001\u0000\u0000\u0000Q\u0081\u0005\u001b\u0000\u0000RS\u0005"+
		"\u0004\u0000\u0000ST\u0003\b\u0004\u0000TU\u0005\n\u0000\u0000UV\u0003"+
		"\b\u0004\u0000VW\u0005\u0002\u0000\u0000WX\u0003\b\u0004\u0000XY\u0005"+
		"\u0003\u0000\u0000Y\u0081\u0001\u0000\u0000\u0000Z[\u0005\u000b\u0000"+
		"\u0000[\\\u0003\b\u0004\u0000\\]\u0005\b\u0000\u0000]^\u0003\b\u0004\u0000"+
		"^_\u0005\t\u0000\u0000_\u0081\u0001\u0000\u0000\u0000`d\u0005\u0016\u0000"+
		"\u0000ab\u0003\b\u0004\u0000bc\u0005\u0015\u0000\u0000ce\u0001\u0000\u0000"+
		"\u0000da\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000fd\u0001\u0000"+
		"\u0000\u0000fg\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000hi\u0005"+
		"\u0017\u0000\u0000i\u0081\u0001\u0000\u0000\u0000jk\u0005\u0010\u0000"+
		"\u0000k\u0081\u0003\n\u0005\u0000lm\u0005\f\u0000\u0000m\u0081\u0005\u0013"+
		"\u0000\u0000no\u0005\u001e\u0000\u0000o\u0081\u0003\b\u0004\u0013pq\u0005"+
		"\u0007\u0000\u0000q\u0081\u0003\b\u0004\u0012rs\u0005\r\u0000\u0000s\u0081"+
		"\u0003\b\u0004\btu\u0005\u001a\u0000\u0000uv\u0003\b\u0004\u0000vw\u0005"+
		"\u001b\u0000\u0000w\u0081\u0001\u0000\u0000\u0000x\u0081\u0005\u0012\u0000"+
		"\u0000y\u0081\u0005\u0011\u0000\u0000z\u0081\u0005\u0014\u0000\u0000{"+
		"\u0081\u0005\u000f\u0000\u0000|\u0081\u0005\u000e\u0000\u0000}~\u0005"+
		"\u0012\u0000\u0000~\u007f\u0005&\u0000\u0000\u007f\u0081\u0003\b\u0004"+
		"\u0001\u0080D\u0001\u0000\u0000\u0000\u0080R\u0001\u0000\u0000\u0000\u0080"+
		"Z\u0001\u0000\u0000\u0000\u0080`\u0001\u0000\u0000\u0000\u0080j\u0001"+
		"\u0000\u0000\u0000\u0080l\u0001\u0000\u0000\u0000\u0080n\u0001\u0000\u0000"+
		"\u0000\u0080p\u0001\u0000\u0000\u0000\u0080r\u0001\u0000\u0000\u0000\u0080"+
		"t\u0001\u0000\u0000\u0000\u0080x\u0001\u0000\u0000\u0000\u0080y\u0001"+
		"\u0000\u0000\u0000\u0080z\u0001\u0000\u0000\u0000\u0080{\u0001\u0000\u0000"+
		"\u0000\u0080|\u0001\u0000\u0000\u0000\u0080}\u0001\u0000\u0000\u0000\u0081"+
		"\u00b2\u0001\u0000\u0000\u0000\u0082\u0083\n\u0011\u0000\u0000\u0083\u0084"+
		"\u0005\u001f\u0000\u0000\u0084\u00b1\u0003\b\u0004\u0012\u0085\u0086\n"+
		"\u0010\u0000\u0000\u0086\u0087\u0005\"\u0000\u0000\u0087\u00b1\u0003\b"+
		"\u0004\u0011\u0088\u0089\n\u000f\u0000\u0000\u0089\u008a\u0005 \u0000"+
		"\u0000\u008a\u00b1\u0003\b\u0004\u0010\u008b\u008c\n\u000e\u0000\u0000"+
		"\u008c\u008d\u0005!\u0000\u0000\u008d\u00b1\u0003\b\u0004\u000f\u008e"+
		"\u008f\n\r\u0000\u0000\u008f\u0090\u0005%\u0000\u0000\u0090\u00b1\u0003"+
		"\b\u0004\u000e\u0091\u0092\n\f\u0000\u0000\u0092\u0093\u0005$\u0000\u0000"+
		"\u0093\u00b1\u0003\b\u0004\r\u0094\u0095\n\u000b\u0000\u0000\u0095\u0096"+
		"\u0005#\u0000\u0000\u0096\u00b1\u0003\b\u0004\f\u0097\u0098\n\n\u0000"+
		"\u0000\u0098\u0099\u0005\'\u0000\u0000\u0099\u00b1\u0003\b\u0004\u000b"+
		"\u009a\u009b\n\t\u0000\u0000\u009b\u009c\u0005(\u0000\u0000\u009c\u00b1"+
		"\u0003\b\u0004\n\u009d\u00a0\n\u001a\u0000\u0000\u009e\u009f\u0005\u001d"+
		"\u0000\u0000\u009f\u00a1\u0005\u0013\u0000\u0000\u00a0\u009e\u0001\u0000"+
		"\u0000\u0000\u00a0\u00a1\u0001\u0000\u0000\u0000\u00a1\u00a2\u0001\u0000"+
		"\u0000\u0000\u00a2\u00a3\u0005\u001c\u0000\u0000\u00a3\u00a4\u0005\u0012"+
		"\u0000\u0000\u00a4\u00ad\u0005\u001a\u0000\u0000\u00a5\u00aa\u0003\b\u0004"+
		"\u0000\u00a6\u00a7\u0005\u0019\u0000\u0000\u00a7\u00a9\u0003\b\u0004\u0000"+
		"\u00a8\u00a6\u0001\u0000\u0000\u0000\u00a9\u00ac\u0001\u0000\u0000\u0000"+
		"\u00aa\u00a8\u0001\u0000\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000\u0000"+
		"\u00ab\u00ae\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000"+
		"\u00ad\u00a5\u0001\u0000\u0000\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000"+
		"\u00ae\u00af\u0001\u0000\u0000\u0000\u00af\u00b1\u0005\u001b\u0000\u0000"+
		"\u00b0\u0082\u0001\u0000\u0000\u0000\u00b0\u0085\u0001\u0000\u0000\u0000"+
		"\u00b0\u0088\u0001\u0000\u0000\u0000\u00b0\u008b\u0001\u0000\u0000\u0000"+
		"\u00b0\u008e\u0001\u0000\u0000\u0000\u00b0\u0091\u0001\u0000\u0000\u0000"+
		"\u00b0\u0094\u0001\u0000\u0000\u0000\u00b0\u0097\u0001\u0000\u0000\u0000"+
		"\u00b0\u009a\u0001\u0000\u0000\u0000\u00b0\u009d\u0001\u0000\u0000\u0000"+
		"\u00b1\u00b4\u0001\u0000\u0000\u0000\u00b2\u00b0\u0001\u0000\u0000\u0000"+
		"\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3\t\u0001\u0000\u0000\u0000\u00b4"+
		"\u00b2\u0001\u0000\u0000\u0000\u00b5\u00b6\u0005\u0012\u0000\u0000\u00b6"+
		"\u00b7\u0005\u0018\u0000\u0000\u00b7\u00b8\u0005\u0013\u0000\u0000\u00b8"+
		"\u00b9\u0005\u0019\u0000\u0000\u00b9\u00d0\u0003\n\u0005\u0000\u00ba\u00bb"+
		"\u0005\u0012\u0000\u0000\u00bb\u00bc\u0005\u0018\u0000\u0000\u00bc\u00bd"+
		"\u0005\u0013\u0000\u0000\u00bd\u00be\u0005\u0005\u0000\u0000\u00be\u00d0"+
		"\u0003\b\u0004\u0000\u00bf\u00c0\u0005\u0012\u0000\u0000\u00c0\u00c1\u0005"+
		"\u0018\u0000\u0000\u00c1\u00c2\u0005\u0013\u0000\u0000\u00c2\u00c3\u0005"+
		"&\u0000\u0000\u00c3\u00c4\u0003\b\u0004\u0000\u00c4\u00c5\u0005\u0019"+
		"\u0000\u0000\u00c5\u00c6\u0003\n\u0005\u0000\u00c6\u00d0\u0001\u0000\u0000"+
		"\u0000\u00c7\u00c8\u0005\u0012\u0000\u0000\u00c8\u00c9\u0005\u0018\u0000"+
		"\u0000\u00c9\u00ca\u0005\u0013\u0000\u0000\u00ca\u00cb\u0005&\u0000\u0000"+
		"\u00cb\u00cc\u0003\b\u0004\u0000\u00cc\u00cd\u0005\u0005\u0000\u0000\u00cd"+
		"\u00ce\u0003\b\u0004\u0000\u00ce\u00d0\u0001\u0000\u0000\u0000\u00cf\u00b5"+
		"\u0001\u0000\u0000\u0000\u00cf\u00ba\u0001\u0000\u0000\u0000\u00cf\u00bf"+
		"\u0001\u0000\u0000\u0000\u00cf\u00c7\u0001\u0000\u0000\u0000\u00d0\u000b"+
		"\u0001\u0000\u0000\u0000\u0011\u0011\u0017\u001f+.<>LOf\u0080\u00a0\u00aa"+
		"\u00ad\u00b0\u00b2\u00cf";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}