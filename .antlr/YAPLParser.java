// Generated from c:\Users\PARK JONGHYUN\Desktop\Universidad\Cuarto año\Segundo ciclo\compiladores\Lab0_UVG_COMPILADORES_2023-1\YAPL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLParser extends Parser {
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
	public static final int
		RULE_program = 0, RULE_classDefine = 1, RULE_inherit = 2, RULE_feature = 3, 
		RULE_formal = 4, RULE_expr = 5, RULE_let_expr = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "classDefine", "inherit", "feature", "formal", "expr", "let_expr"
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
	public static class StartContext extends ProgramContext {
		public List<ClassDefineContext> classDefine() {
			return getRuleContexts(ClassDefineContext.class);
		}
		public ClassDefineContext classDefine(int i) {
			return getRuleContext(ClassDefineContext.class,i);
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
				setState(14);
				classDefine();
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
	public static class DefClaseContext extends ClassDefineContext {
		public TerminalNode CLASS() { return getToken(YAPLParser.CLASS, 0); }
		public TerminalNode CLASSTYPE() { return getToken(YAPLParser.CLASSTYPE, 0); }
		public TerminalNode OPENBRACE() { return getToken(YAPLParser.OPENBRACE, 0); }
		public TerminalNode CLOSEBRACE() { return getToken(YAPLParser.CLOSEBRACE, 0); }
		public List<TerminalNode> SEMICOLON() { return getTokens(YAPLParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YAPLParser.SEMICOLON, i);
		}
		public InheritContext inherit() {
			return getRuleContext(InheritContext.class,0);
		}
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
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
			match(CLASSTYPE);
			setState(22);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITS) {
				{
				setState(21);
				inherit();
				}
			}

			setState(24);
			match(OPENBRACE);
			setState(30);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(25);
				feature();
				setState(26);
				match(SEMICOLON);
				}
				}
				setState(32);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(33);
			match(CLOSEBRACE);
			setState(34);
			match(SEMICOLON);
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

	public static class InheritContext extends ParserRuleContext {
		public InheritContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inherit; }
	 
		public InheritContext() { }
		public void copyFrom(InheritContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class InheritsContext extends InheritContext {
		public TerminalNode INHERITS() { return getToken(YAPLParser.INHERITS, 0); }
		public TerminalNode CLASSTYPE() { return getToken(YAPLParser.CLASSTYPE, 0); }
		public InheritsContext(InheritContext ctx) { copyFrom(ctx); }
	}

	public final InheritContext inherit() throws RecognitionException {
		InheritContext _localctx = new InheritContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_inherit);
		try {
			_localctx = new InheritsContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(INHERITS);
			setState(37);
			match(CLASSTYPE);
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

	public static class FeatureContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode OPENPARENTHESES() { return getToken(YAPLParser.OPENPARENTHESES, 0); }
		public TerminalNode CLOSEPARENTHESES() { return getToken(YAPLParser.CLOSEPARENTHESES, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode CLASSTYPE() { return getToken(YAPLParser.CLASSTYPE, 0); }
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
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_feature);
		int _la;
		try {
			setState(65);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(39);
				match(ID);
				setState(40);
				match(OPENPARENTHESES);
				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(41);
					formal();
					setState(46);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(42);
						match(COMMA);
						setState(43);
						formal();
						}
						}
						setState(48);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(51);
				match(CLOSEPARENTHESES);
				setState(52);
				match(COLON);
				setState(53);
				match(CLASSTYPE);
				setState(54);
				match(OPENBRACE);
				setState(55);
				expr(0);
				setState(56);
				match(CLOSEBRACE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(58);
				match(ID);
				setState(59);
				match(COLON);
				setState(60);
				match(CLASSTYPE);
				setState(63);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(61);
					match(ASSIGN);
					setState(62);
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
	public static class FormlContext extends FormalContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode CLASSTYPE() { return getToken(YAPLParser.CLASSTYPE, 0); }
		public FormlContext(FormalContext ctx) { copyFrom(ctx); }
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_formal);
		try {
			_localctx = new FormlContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(ID);
			setState(68);
			match(COLON);
			setState(69);
			match(CLASSTYPE);
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
	public static class VoidContext extends ExprContext {
		public TerminalNode ISVOID() { return getToken(YAPLParser.ISVOID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public VoidContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class InvertContext extends ExprContext {
		public TerminalNode INTEGER_NEGATIVE() { return getToken(YAPLParser.INTEGER_NEGATIVE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public InvertContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class StringContext extends ExprContext {
		public TerminalNode STRING() { return getToken(YAPLParser.STRING, 0); }
		public StringContext(ExprContext ctx) { copyFrom(ctx); }
	}
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
	public static class FactExprContext extends ExprContext {
		public TerminalNode OPENPARENTHESES() { return getToken(YAPLParser.OPENPARENTHESES, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSEPARENTHESES() { return getToken(YAPLParser.CLOSEPARENTHESES, 0); }
		public FactExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
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
	public static class NumContext extends ExprContext {
		public TerminalNode NUM() { return getToken(YAPLParser.NUM, 0); }
		public NumContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class FalseContext extends ExprContext {
		public TerminalNode FALSE() { return getToken(YAPLParser.FALSE, 0); }
		public FalseContext(ExprContext ctx) { copyFrom(ctx); }
	}
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
	public static class NotContext extends ExprContext {
		public TerminalNode NOT() { return getToken(YAPLParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NotContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class NewObjectContext extends ExprContext {
		public TerminalNode NEW() { return getToken(YAPLParser.NEW, 0); }
		public TerminalNode CLASSTYPE() { return getToken(YAPLParser.CLASSTYPE, 0); }
		public NewObjectContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class TrueContext extends ExprContext {
		public TerminalNode TRUE() { return getToken(YAPLParser.TRUE, 0); }
		public TrueContext(ExprContext ctx) { copyFrom(ctx); }
	}
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
	public static class LetContext extends ExprContext {
		public TerminalNode LET() { return getToken(YAPLParser.LET, 0); }
		public Let_exprContext let_expr() {
			return getRuleContext(Let_exprContext.class,0);
		}
		public LetContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IdContext extends ExprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public IdContext(ExprContext ctx) { copyFrom(ctx); }
	}
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
	public static class AssignContext extends ExprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignContext(ExprContext ctx) { copyFrom(ctx); }
	}
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
		public TerminalNode CLASSTYPE() { return getToken(YAPLParser.CLASSTYPE, 0); }
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
		int _startState = 10;
		enterRecursionRule(_localctx, 10, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				_localctx = new AssignContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(72);
				match(ID);
				setState(73);
				match(ASSIGN);
				setState(74);
				expr(24);
				}
				break;
			case 2:
				{
				_localctx = new OwnMethodCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(75);
				match(ID);
				setState(76);
				match(OPENPARENTHESES);
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FALSE) | (1L << TRUE) | (1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << NUM) | (1L << ID) | (1L << STRING) | (1L << OPENBRACE) | (1L << OPENPARENTHESES) | (1L << INTEGER_NEGATIVE))) != 0)) {
					{
					setState(77);
					expr(0);
					setState(82);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(78);
						match(COMMA);
						setState(79);
						expr(0);
						}
						}
						setState(84);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(87);
				match(CLOSEPARENTHESES);
				}
				break;
			case 3:
				{
				_localctx = new IfContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(88);
				match(IF);
				setState(89);
				expr(0);
				setState(90);
				match(THEN);
				setState(91);
				expr(0);
				setState(92);
				match(ELSE);
				setState(93);
				expr(0);
				setState(94);
				match(FI);
				}
				break;
			case 4:
				{
				_localctx = new WhileContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(96);
				match(WHILE);
				setState(97);
				expr(0);
				setState(98);
				match(LOOP);
				setState(99);
				expr(0);
				setState(100);
				match(POOL);
				}
				break;
			case 5:
				{
				_localctx = new BlockContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(102);
				match(OPENBRACE);
				setState(106); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(103);
					expr(0);
					setState(104);
					match(SEMICOLON);
					}
					}
					setState(108); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FALSE) | (1L << TRUE) | (1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << NUM) | (1L << ID) | (1L << STRING) | (1L << OPENBRACE) | (1L << OPENPARENTHESES) | (1L << INTEGER_NEGATIVE))) != 0) );
				setState(110);
				match(CLOSEBRACE);
				}
				break;
			case 6:
				{
				_localctx = new LetContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(112);
				match(LET);
				setState(113);
				let_expr();
				}
				break;
			case 7:
				{
				_localctx = new NewObjectContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(114);
				match(NEW);
				setState(115);
				match(CLASSTYPE);
				}
				break;
			case 8:
				{
				_localctx = new VoidContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(116);
				match(ISVOID);
				setState(117);
				expr(16);
				}
				break;
			case 9:
				{
				_localctx = new InvertContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(118);
				match(INTEGER_NEGATIVE);
				setState(119);
				expr(11);
				}
				break;
			case 10:
				{
				_localctx = new NotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(120);
				match(NOT);
				setState(121);
				expr(7);
				}
				break;
			case 11:
				{
				_localctx = new FactExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(122);
				match(OPENPARENTHESES);
				setState(123);
				expr(0);
				setState(124);
				match(CLOSEPARENTHESES);
				}
				break;
			case 12:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(126);
				match(ID);
				}
				break;
			case 13:
				{
				_localctx = new NumContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(127);
				match(NUM);
				}
				break;
			case 14:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(128);
				match(STRING);
				}
				break;
			case 15:
				{
				_localctx = new TrueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(129);
				match(TRUE);
				}
				break;
			case 16:
				{
				_localctx = new FalseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(130);
				match(FALSE);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(175);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(173);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
					case 1:
						{
						_localctx = new AddContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(133);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(134);
						match(ADD);
						setState(135);
						expr(16);
						}
						break;
					case 2:
						{
						_localctx = new SubContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(136);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(137);
						match(SUB);
						setState(138);
						expr(15);
						}
						break;
					case 3:
						{
						_localctx = new MulContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(139);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(140);
						match(MUL);
						setState(141);
						expr(14);
						}
						break;
					case 4:
						{
						_localctx = new DivContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(142);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(143);
						match(DIV);
						setState(144);
						expr(13);
						}
						break;
					case 5:
						{
						_localctx = new LtContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(145);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(146);
						match(LT);
						setState(147);
						expr(11);
						}
						break;
					case 6:
						{
						_localctx = new LteqContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(148);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(149);
						match(LTEQ);
						setState(150);
						expr(10);
						}
						break;
					case 7:
						{
						_localctx = new EqualContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(151);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(152);
						match(EQUAL);
						setState(153);
						expr(9);
						}
						break;
					case 8:
						{
						_localctx = new MethodCallContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(154);
						if (!(precpred(_ctx, 23))) throw new FailedPredicateException(this, "precpred(_ctx, 23)");
						setState(157);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==AT) {
							{
							setState(155);
							match(AT);
							setState(156);
							match(CLASSTYPE);
							}
						}

						setState(159);
						match(DOT);
						setState(160);
						match(ID);
						setState(161);
						match(OPENPARENTHESES);
						setState(170);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FALSE) | (1L << TRUE) | (1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << NUM) | (1L << ID) | (1L << STRING) | (1L << OPENBRACE) | (1L << OPENPARENTHESES) | (1L << INTEGER_NEGATIVE))) != 0)) {
							{
							setState(162);
							expr(0);
							setState(167);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==COMMA) {
								{
								{
								setState(163);
								match(COMMA);
								setState(164);
								expr(0);
								}
								}
								setState(169);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(172);
						match(CLOSEPARENTHESES);
						}
						break;
					}
					} 
				}
				setState(177);
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

	public static class Let_exprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode CLASSTYPE() { return getToken(YAPLParser.CLASSTYPE, 0); }
		public TerminalNode COMMA() { return getToken(YAPLParser.COMMA, 0); }
		public Let_exprContext let_expr() {
			return getRuleContext(Let_exprContext.class,0);
		}
		public TerminalNode IN() { return getToken(YAPLParser.IN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public Let_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_let_expr; }
	}

	public final Let_exprContext let_expr() throws RecognitionException {
		Let_exprContext _localctx = new Let_exprContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_let_expr);
		try {
			setState(204);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				match(ID);
				setState(179);
				match(COLON);
				setState(180);
				match(CLASSTYPE);
				setState(181);
				match(COMMA);
				setState(182);
				let_expr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(183);
				match(ID);
				setState(184);
				match(COLON);
				setState(185);
				match(CLASSTYPE);
				setState(186);
				match(IN);
				setState(187);
				expr(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(188);
				match(ID);
				setState(189);
				match(COLON);
				setState(190);
				match(CLASSTYPE);
				setState(191);
				match(ASSIGN);
				setState(192);
				expr(0);
				setState(193);
				match(COMMA);
				setState(194);
				let_expr();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(196);
				match(ID);
				setState(197);
				match(COLON);
				setState(198);
				match(CLASSTYPE);
				setState(199);
				match(ASSIGN);
				setState(200);
				expr(0);
				setState(201);
				match(IN);
				setState(202);
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
		case 5:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 15);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 12);
		case 4:
			return precpred(_ctx, 10);
		case 5:
			return precpred(_ctx, 9);
		case 6:
			return precpred(_ctx, 8);
		case 7:
			return precpred(_ctx, 23);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,\u00d1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\6\2\22\n\2\r\2\16\2"+
		"\23\3\3\3\3\3\3\5\3\31\n\3\3\3\3\3\3\3\3\3\7\3\37\n\3\f\3\16\3\"\13\3"+
		"\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\7\5/\n\5\f\5\16\5\62\13\5"+
		"\5\5\64\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5B\n\5\5"+
		"\5D\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7S\n\7\f"+
		"\7\16\7V\13\7\5\7X\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\6\7m\n\7\r\7\16\7n\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0086"+
		"\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a0\n\7\3\7\3\7\3\7\3\7\3\7\3\7\7"+
		"\7\u00a8\n\7\f\7\16\7\u00ab\13\7\5\7\u00ad\n\7\3\7\7\7\u00b0\n\7\f\7\16"+
		"\7\u00b3\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00cf\n\b\3\b\2\3"+
		"\f\t\2\4\6\b\n\f\16\2\2\2\u00f0\2\21\3\2\2\2\4\25\3\2\2\2\6&\3\2\2\2\b"+
		"C\3\2\2\2\nE\3\2\2\2\f\u0085\3\2\2\2\16\u00ce\3\2\2\2\20\22\5\4\3\2\21"+
		"\20\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2\2\25"+
		"\26\7\3\2\2\26\30\7\25\2\2\27\31\5\6\4\2\30\27\3\2\2\2\30\31\3\2\2\2\31"+
		"\32\3\2\2\2\32 \7\30\2\2\33\34\5\b\5\2\34\35\7\27\2\2\35\37\3\2\2\2\36"+
		"\33\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!#\3\2\2\2\" \3\2\2\2#$"+
		"\7\31\2\2$%\7\27\2\2%\5\3\2\2\2&\'\7\n\2\2\'(\7\25\2\2(\7\3\2\2\2)*\7"+
		"\24\2\2*\63\7\34\2\2+\60\5\n\6\2,-\7\33\2\2-/\5\n\6\2.,\3\2\2\2/\62\3"+
		"\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\63+\3\2\2"+
		"\2\63\64\3\2\2\2\64\65\3\2\2\2\65\66\7\35\2\2\66\67\7\32\2\2\678\7\25"+
		"\2\289\7\30\2\29:\5\f\7\2:;\7\31\2\2;D\3\2\2\2<=\7\24\2\2=>\7\32\2\2>"+
		"A\7\25\2\2?@\7(\2\2@B\5\f\7\2A?\3\2\2\2AB\3\2\2\2BD\3\2\2\2C)\3\2\2\2"+
		"C<\3\2\2\2D\t\3\2\2\2EF\7\24\2\2FG\7\32\2\2GH\7\25\2\2H\13\3\2\2\2IJ\b"+
		"\7\1\2JK\7\24\2\2KL\7(\2\2L\u0086\5\f\7\32MN\7\24\2\2NW\7\34\2\2OT\5\f"+
		"\7\2PQ\7\33\2\2QS\5\f\7\2RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UX\3"+
		"\2\2\2VT\3\2\2\2WO\3\2\2\2WX\3\2\2\2XY\3\2\2\2Y\u0086\7\35\2\2Z[\7\b\2"+
		"\2[\\\5\f\7\2\\]\7\16\2\2]^\5\f\7\2^_\7\4\2\2_`\5\f\7\2`a\7\7\2\2a\u0086"+
		"\3\2\2\2bc\7\17\2\2cd\5\f\7\2de\7\f\2\2ef\5\f\7\2fg\7\r\2\2g\u0086\3\2"+
		"\2\2hl\7\30\2\2ij\5\f\7\2jk\7\27\2\2km\3\2\2\2li\3\2\2\2mn\3\2\2\2nl\3"+
		"\2\2\2no\3\2\2\2op\3\2\2\2pq\7\31\2\2q\u0086\3\2\2\2rs\7\22\2\2s\u0086"+
		"\5\16\b\2tu\7\20\2\2u\u0086\7\25\2\2vw\7\13\2\2w\u0086\5\f\7\22xy\7 \2"+
		"\2y\u0086\5\f\7\rz{\7\21\2\2{\u0086\5\f\7\t|}\7\34\2\2}~\5\f\7\2~\177"+
		"\7\35\2\2\177\u0086\3\2\2\2\u0080\u0086\7\24\2\2\u0081\u0086\7\23\2\2"+
		"\u0082\u0086\7\26\2\2\u0083\u0086\7\6\2\2\u0084\u0086\7\5\2\2\u0085I\3"+
		"\2\2\2\u0085M\3\2\2\2\u0085Z\3\2\2\2\u0085b\3\2\2\2\u0085h\3\2\2\2\u0085"+
		"r\3\2\2\2\u0085t\3\2\2\2\u0085v\3\2\2\2\u0085x\3\2\2\2\u0085z\3\2\2\2"+
		"\u0085|\3\2\2\2\u0085\u0080\3\2\2\2\u0085\u0081\3\2\2\2\u0085\u0082\3"+
		"\2\2\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086\u00b1\3\2\2\2\u0087"+
		"\u0088\f\21\2\2\u0088\u0089\7!\2\2\u0089\u00b0\5\f\7\22\u008a\u008b\f"+
		"\20\2\2\u008b\u008c\7\"\2\2\u008c\u00b0\5\f\7\21\u008d\u008e\f\17\2\2"+
		"\u008e\u008f\7#\2\2\u008f\u00b0\5\f\7\20\u0090\u0091\f\16\2\2\u0091\u0092"+
		"\7$\2\2\u0092\u00b0\5\f\7\17\u0093\u0094\f\f\2\2\u0094\u0095\7&\2\2\u0095"+
		"\u00b0\5\f\7\r\u0096\u0097\f\13\2\2\u0097\u0098\7\'\2\2\u0098\u00b0\5"+
		"\f\7\f\u0099\u009a\f\n\2\2\u009a\u009b\7%\2\2\u009b\u00b0\5\f\7\13\u009c"+
		"\u009f\f\31\2\2\u009d\u009e\7\37\2\2\u009e\u00a0\7\25\2\2\u009f\u009d"+
		"\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\7\36\2\2"+
		"\u00a2\u00a3\7\24\2\2\u00a3\u00ac\7\34\2\2\u00a4\u00a9\5\f\7\2\u00a5\u00a6"+
		"\7\33\2\2\u00a6\u00a8\5\f\7\2\u00a7\u00a5\3\2\2\2\u00a8\u00ab\3\2\2\2"+
		"\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9"+
		"\3\2\2\2\u00ac\u00a4\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae"+
		"\u00b0\7\35\2\2\u00af\u0087\3\2\2\2\u00af\u008a\3\2\2\2\u00af\u008d\3"+
		"\2\2\2\u00af\u0090\3\2\2\2\u00af\u0093\3\2\2\2\u00af\u0096\3\2\2\2\u00af"+
		"\u0099\3\2\2\2\u00af\u009c\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2"+
		"\2\2\u00b1\u00b2\3\2\2\2\u00b2\r\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5"+
		"\7\24\2\2\u00b5\u00b6\7\32\2\2\u00b6\u00b7\7\25\2\2\u00b7\u00b8\7\33\2"+
		"\2\u00b8\u00cf\5\16\b\2\u00b9\u00ba\7\24\2\2\u00ba\u00bb\7\32\2\2\u00bb"+
		"\u00bc\7\25\2\2\u00bc\u00bd\7\t\2\2\u00bd\u00cf\5\f\7\2\u00be\u00bf\7"+
		"\24\2\2\u00bf\u00c0\7\32\2\2\u00c0\u00c1\7\25\2\2\u00c1\u00c2\7(\2\2\u00c2"+
		"\u00c3\5\f\7\2\u00c3\u00c4\7\33\2\2\u00c4\u00c5\5\16\b\2\u00c5\u00cf\3"+
		"\2\2\2\u00c6\u00c7\7\24\2\2\u00c7\u00c8\7\32\2\2\u00c8\u00c9\7\25\2\2"+
		"\u00c9\u00ca\7(\2\2\u00ca\u00cb\5\f\7\2\u00cb\u00cc\7\t\2\2\u00cc\u00cd"+
		"\5\f\7\2\u00cd\u00cf\3\2\2\2\u00ce\u00b4\3\2\2\2\u00ce\u00b9\3\2\2\2\u00ce"+
		"\u00be\3\2\2\2\u00ce\u00c6\3\2\2\2\u00cf\17\3\2\2\2\23\23\30 \60\63AC"+
		"TWn\u0085\u009f\u00a9\u00ac\u00af\u00b1\u00ce";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}